from fastapi import FastAPI, HTTPException
import json
import aiofiles


app = FastAPI()
"""
def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)

    return users
"""


@app.get("/users/")
async def read_user():
    async with aiofiles.open("data/users.json", mode="r") as stream:
        return json.load(stream)


@app.get("/user/info")
def read_user(id: int):
    with open("data/users.json") as stream:
        users = json.load(stream)
        user = next((user for user in users if user.get("id") == id), None)

        if user is not None:
            return user
        else:
            raise HTTPException(
                status_code=404, detail=f"Пользователь с таким id не найден!!! {id}"
            )


"""
def read_questions(position: int):
    with open('data/questions.json') as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            return question
"""


@app.get("/user/questions")
async def read_questions(position: int):
    with open("PRAC-BCND-2/data/questions.json") as stream:
        questions = json.load(stream)
        for question in questions:
            if question.get("position") == position:
                return question
            else:
                print("error: Вопроса на такой позиции не существует!!!")


"""
def read_alternatives(question_id: int):
    alternatives_question = []
    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question
"""


@app.get("/user/answers")
async def read_answers(user_id: int):
    async with aiofiles.open("data/answers.json", mode="r") as stream:
        answers = json.load(stream)

        user_answer = next(
            (answer for answer in answers if answer.get("user_id") == user_id), None
        )

        if user_answer is None:
            raise HTTPException(
                status_code=404, detail="Пользователь с таким id не найден!!!"
            )

        async with aiofiles.open("data/alternatives.json", mode="r") as alt_stream:
            alternatives = json.loads(await alt_stream.read())
            alternative = next(
                (
                    alt
                    for alt in alternatives
                    if alt["id"] == user_answer["alternative_id"]
                ),
                None,
            )

            if alternative is None:
                raise HTTPException(
                    status_code=404, detail="Альтернатива с таким id не найдена!!!"
                )

            return alternative


"""
def create_answer(payload):
    answers = []
    result = []

    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for question in payload['answers']:
        for alternative in alternatives:
            if alternative['question_id'] == question['question_id']:
                answers.append(alternative['alternative'])
                break

    with open('data/cars.json') as stream:
        cars = json.load(stream)

    for car in cars:
        if answers[0] in car.values() and answers[1] in car.values() and answers[2] in car.values():
            result.append(car)

    return result
"""


@app.post("/user/answer/{id}")
async def create_answer(payload: dict, id: int):
    with open("data/answers.json") as stream:
        answers = json.load(stream)
        for answer in answers:
            if answer.get("user_id") == id and payload.get("question_id") == answer.get(
                "question_id"
            ):
                with open("data/alternatives.json") as stream:
                    alternatives = json.load(stream)
                    for alternative in alternatives:
                        if answer.get("question_id") == alternative.get("question_id"):
                            alternative["alternative"] = payload.get("answer")


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
