import logging
import uvicorn
import socketio
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="./static"), name="static")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:7777", "http://127.0.0.1:7777"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Socket.IO server
sio = socketio.AsyncServer(cors_allowed_origins=["http://localhost:7777", "http://127.0.0.1:7777"], async_mode="asgi")
app.mount("/socket.io", socketio.ASGIApp(sio, other_asgi_app=app))

# Storage for connected users and video timing
connected_users = {}
video_start_time = {}
video_duration = {}
video_playing = {}  # Track the video playing state for each room

def init_or_update_video_timing(room, duration):
    current_time = time.time()
    if room not in video_start_time:
        # Initialize the video timing and duration if it's the first access for this room
        video_start_time[room] = {
            'start': current_time,
            'next': current_time + duration,
        }
        video_duration[room] = duration  # Properly initialize the duration
        video_playing[room] = False  # Initialize the playing state
        logger.info(f"Initialized video timing for room {room} with start: {current_time}, next: {current_time + duration}")
    else:
        # Only update if the current time is past the 'next' scheduled start time
        if current_time > video_start_time[room]['next']:
            previous_next = video_start_time[room]['next']
            video_start_time[room]['next'] = current_time + video_duration[room]
            logger.info(f"Updated video timing for room {room} from previous next: {previous_next} to new next: {video_start_time[room]['next']}")



@app.get("/", response_class=HTMLResponse)
def render_socketio_page(fids_id: str, template_id: int, duration: int = Query(..., gt=0)):
    logger.info(f"Rendering page for fids_id: {fids_id}, template_id: {template_id}, duration: {duration}")
    return HTMLResponse(content=f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Socket.IO Client</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.0/socket.io.js"></script>
</head>
<body>
    <div id="user-info"></div>
    <video id="sync-video" width="400" controls muted>
        <source src="/static/video.mp4" type="video/mp4">
        Your browser does not support HTML video.
    </video>
    <script>
        const socket = io("http://127.0.0.1:7777", {{
            auth: {{ template_id: {template_id}, fids_id: "{fids_id}" }}
        }});
        socket.on("connect", () => {{
            console.log("Connected with Socket.IO server");
            socket.emit("check_in", {{ fids_id: "{fids_id}", template_id: {template_id}, duration: {duration} }});
        }});
        socket.on("start_video", (data) => {{
            console.log("Received start_video with startTime:", data.startTime);
            const video = document.getElementById("sync-video");
            const currentTime = Date.now() / 1000;
            const waitTime = data.startTime - currentTime;
            console.log("Calculated waitTime:", waitTime);
            if (waitTime > 0) {{
                setTimeout(() => {{
                    video.currentTime = 0;
                    video.play().catch(error => console.error("Error playing video:", error));
                }}, waitTime * 1000);
            }} else {{
                console.log("Incorrect waitTime, attempting immediate play.");
                video.currentTime = currentTime - data.startTime;
                video.play().catch(error => console.error("Error playing video:", error));
            }}
        }});
        socket.on("disconnect", () => console.log("Disconnected from Socket.IO server"));
        socket.on("update_users", (users) => {{
            document.getElementById("user-info").innerHTML = "Connected users: <br>" +
                users.map(user => "ID: " + user.sid + ", IP: " + user.ip).join("<br>");
        }});
        const video = document.getElementById("sync-video");
        video.onended = () => {{
            socket.emit("video_ended", {{ fids_id: "{fids_id}", template_id: {template_id} }});
        }};
    </script>
</body>
</html>
    """)

@app.get("/next_start_time")
async def get_next_start_time(fids_id: str, template_id: int):
    room = f"{fids_id}-{template_id}"
    if room in video_start_time:
        logger.info(f"Next start time for room {room} is {video_start_time[room]['next']}")
        return JSONResponse({"nextStartTime": video_start_time[room]['next']})
    logger.info(f"No start time found for room {room}")
    return JSONResponse({"nextStartTime": None})

@sio.event
async def check_in(sid, data):
    room = f"{data['fids_id']}-{data['template_id']}"
    duration = data.get('duration', 30)  # Use a default if not provided
    init_or_update_video_timing(room, duration)
    logger.info(f"Client {sid} checked in to room {room}, waiting for current playback to end.")
    if video_playing[room]:
        # Emit the start time for the current playback to the new client
        await sio.emit("start_video", {"startTime": video_start_time[room]['start']}, room=sid)
    else:
        logger.info(f"No video is currently playing in room {room}, starting new playback.")
        video_playing[room] = True  # Mark video as playing
        await sio.emit("start_video", {"startTime": video_start_time[room]['next']}, room=room)



@sio.event
async def video_ended(sid, data):
    room = f"{data['fids_id']}-{data['template_id']}"
    video_playing[room] = False
    logger.info(f"Video ended for client {sid} in room {room}, current users: {connected_users[room]}")
    init_or_update_video_timing(room, video_duration[room])
    logger.info(f"Scheduling next start for room {room} with startTime {video_start_time[room]['next']}")
    video_playing[room] = True  # Mark video as playing
    await sio.emit("start_video", {"startTime": video_start_time[room]['next']}, room=room)

@sio.event
async def connect(sid, environ, auth):
    fids_id = auth.get("fids_id")
    template_id = auth.get("template_id")
    room = f"{fids_id}-{template_id}"
    logger.info(f"Client {sid} connected with auth {auth} to room {room}")
    if room not in connected_users:
        connected_users[room] = []
    ip_address = environ.get('REMOTE_ADDR')  # Get the IP address from the environment
    connected_users[room].append({"sid": sid, "ip": ip_address})
    await sio.save_session(sid, {"room": room})
    await sio.enter_room(sid, room)
    logger.info(f"Client {sid} joined room {room}. Current users: {connected_users[room]}")
    await sio.emit("update_users", connected_users[room], room=room)

@sio.event
async def disconnect(sid):
    session = await sio.get_session(sid)
    room = session.get("room")
    if room and sid in [user["sid"] for user in connected_users.get(room, [])]:
        connected_users[room] = [user for user in connected_users[room] if user["sid"] != sid]
        logger.info(f"Client {sid} disconnected from room {room}")
        if not connected_users[room]:
            # Clear video timings if the last user disconnects
            video_start_time.pop(room, None)
            video_duration.pop(room, None)
            video_playing.pop(room, None)
            logger.info(f"Room {room} is now empty. Cleared video timings.")
        else:
            await sio.emit("update_users", connected_users[room], room=room)
            logger.info(f"Updated users for room {room}: {connected_users[room]}")

if __name__ == "__main__":
    uvicorn.run("socket_io:app", host="0.0.0.0", port=7777, reload=True)
