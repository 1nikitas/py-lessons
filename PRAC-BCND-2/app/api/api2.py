from fastapi import FastAPI, HTTPException

from app.db.schemas import CreateUser, DeleteUser, UpdateUser

from app.db.database import Base, engine, SessionLocal

from app.db.models import Answer, Question, User

Base.metadata.create_all(bind=engine)
db=SessionLocal()

app = FastAPI()


@app.get("/users/")
async def read_users():
    users = db.query(User).all()
    return users


@app.get("/user/info")
def read_user(id: int):
    users = db.query(User).all()

    user = next((user for user in users if user.user_id == id), None)

    if user is not None:
        return user
    else:
        raise HTTPException(
            status_code=404, detail=f"Пользователь с таким id не найден!!! {id}"  # noqa: E501
        )


@app.get("/user/questions")
async def read_questions(position: int):
    questions = db.query(Question).all()
    question = next(
        (
            question
            for question in questions
            if question.question_id == position
        ),
        None,
    )
    if question is not None:
        return question
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Вопроса на такой позиции не существует!!! {id}",
        )


@app.get("/user/answers")
async def read_answers(user_id: int):
    answers = db.query(Answer).all()

    user_answers = [answer for answer in answers if answer.user_id == user_id]

    if user_answers == []:
        raise HTTPException(
            status_code=404, detail="Пользователь с таким id не найден!!!"
        )
    return user_answers

@app.post("/user/answer/{id}")
async def create_answer(payload: dict, id: int):
    """

    {
        "status": "success",
        "id": 1,
        "question_id": 1,
        "alternative": "new answer",
        "method": "create/update"

    }
    """

    # Чтение файла answers.json
    answers = db.query(Answer).all()
    answer = next(
        (
            answer
            for answer in answers
            if answer.get("question_id") == payload.get("question_id")
        ),
        None,
    )
    if answer is None:
        # Создаем новый ответ, если его нет
        new_answer = {
            "id": len(answers) + 1,
            "question_id": payload.get("question_id"),
            "alternative": payload.get("alternative"),
        }
        answers.append(new_answer)
        method = "create"
    else:
        # Изменяем существующий ответ
        answer["alternative"] = payload.get("alternative")
        method = "update"

    # Запись обновленного файла answers.json
    async with aiofiles.open("data/answers.json", mode="w") as stream_1:
        await stream_1.write(json.dumps(answers, indent=4))

    # Чтение файла alternatives.json
    async with aiofiles.open("data/alternatives.json", mode="r") as stream_2:
        alternatives_content = await stream_2.read()
        alternatives = json.loads(alternatives_content)
        alternative = next(
            (
                alternative
                for alternative in alternatives
                if alternative.get("question_id") == payload.get("question_id")
            ),
            None,
        )

    if alternative is None:
        # Создаем новый альтернативный ответ, если его нет
        new_alternative = {
            "id": alternatives[-1].get("id") + 1 if alternatives else 1,
            "question_id": payload.get("question_id"),
            "alternative": payload.get("alternative"),
        }
        alternatives.append(new_alternative)
    else:
        # Изменяем существующий альтернативный ответ
        alternative["alternative"] = payload.get("alternative")

    # Запись обновленного файла alternatives.json
    async with aiofiles.open("data/alternatives.json", mode="w") as stream_2:
        await stream_2.write(json.dumps(alternatives, indent=4))

    return {
        "status": "success",
        "user_id": answer["user_id"],
        "alternative_id": answer["alternative_id"],
        "question_id": answer["question_id"],
        "alternative": alternative["alternative"],
        "method": method,
    }


"""
def read_result(user_id: int):
    user_result = []

    with open('data/results.json') as stream:
        results = json.load(stream)

    with open('data/users.json') as stream:
        users = json.load(stream)

    with open('data/cars.json') as stream:
        cars = json.load(stream)

    for result in results:
        if result['user_id'] == user_id:
            for user in users:
                if user['id'] == result['user_id']:
                    user_result.append({'user': user})
                    break

        for car_id in result['cars']:
            for car in cars:
                if car_id == car['id']:
                    user_result.append(car)

    return user_result
"""


@app.post("/user/add")
async def create_user(user: CreateUser):
    async with aiofiles.open("data/users.json", mode="r") as stream_1:
        users_content = await stream_1.read()
        users = json.loads(users_content)
        new_user = {
            "id": len(users) + 1,
            "name": user.name,
            "mail": user.mail,
            "phone": user.phone,
        }
        users.append(new_user)
    async with aiofiles.open("data/users.json", mode="w") as stream_2:
        await stream_2.write(json.dumps(users, indent=4))
    return {
        "Новый пользователь:": {
            "id": len(users) + 1,
            "name": user.name,
            "mail": user.mail,
            "phone": user.phone,
        }
    }


@app.post("/user/delete")
async def delete_user(id: DeleteUser):
    async with aiofiles.open("data/users.json", mode="r") as stream_1:
        users_content = await stream_1.read()
        users = json.loads(users_content)
        user = next((user for user in users if user.get("id") == id), None)
        if user is None:
            raise HTTPException(
                status_code=404, detail="Пользователь с таким id не существует!!!"
            )
        del_user = {
            "id": user.get("id"),
            "name": user.get("name"),
            "mail": user.get("mail"),
            "phone": user.get("phone"),
        }
        user = next(
            (user for user in users if del_user.get("id") == user.get("id")), None
        )
        users.remove(users.index(user))
        async with aiofiles.open("data/users.json", mode="w") as stream_2:
            await stream_2.write(json.dumps(users, indent=4))
        return {
            "Удалённый пользователь:": {
                "id": user.get("id"),
                "name": user.get("name"),
                "mail": user.get("mail"),
                "phone": user.get("phone"),
            }
        }


@app.post("/user/update/{id}")
async def update_user(update: UpdateUser, id: int):
    async with aiofiles.open("app/api/data/users.json", mode="r") as stream_1:
        users_content = await stream_1.read()
        users = json.loads(users_content)
        user = next((user for user in users if user.get("id") == id), None)
        if user is None:
            raise HTTPException(
                status_code=404, detail="Пользователь с таким id не существует!!!"
            )

        update_user = {
            "id": id,
            "name": update.name,
            "mail": update.mail,
            "phone": update.phone,
        }
        users.remove(user)
        users.append(update_user)
    async with aiofiles.open("app/api/data/users.json", mode="w") as stream_2:
        await stream_2.write(json.dumps(users, indent=4))
    return {
        "Обновлённый пользователь:": {
            "id": id,
            "name": update.name,
            "mail": update.mail,
            "phone": update.phone,
        }
    }
