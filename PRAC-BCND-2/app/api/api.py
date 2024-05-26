from fastapi import FastAPI
import json

app = FastAPI()
'''
def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)

    return users
'''

@app.get("/users/")
async def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)
        return users

@app.get("/user/info")
def read_user(id: int):
    with open('data/users.json') as stream:
        users = json.load(stream)
        for user in users:
            if user.get('id') == id:
                return user
        else:
            return {'error': f'Пользователь с таким id не найден!!!{id}'}


'''
def read_questions(position: int):
    with open('data/questions.json') as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            return question
'''

@app.get("/user/questions")
async def read_questions(position: int):
    with open('PRAC-BCND-2/data/questions.json') as stream:
        questions = json.load(stream)
        for question in questions:
            if question.get('position') == position:
                return question
            else:
                print('error: Вопроса на такой позиции не существует!!!')


'''
def read_alternatives(question_id: int):
    alternatives_question = []
    with open('data/alternatives.json') as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            alternatives_question.append(alternative)

    return alternatives_question
'''

@app.get("/user/answers")
async def read_answers(user_id: int):
    with open('data/answers.json') as stream:
        answers = json.load(stream)
        for answer in answers:
            if answer.get('user_id') == user_id:
                with open('data/alternatives.json') as alternatives:
                    for alternative in alternatives:
                        if answer['alternative_id'] == alternative['id']:
                            return alternative
            else: return {'error': 'Пользователь с таким id не найден!!!'}
'''
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
'''

@app.post("/user/answer/{id}")
async def create_answer(payload: dict, id:int):
    with open('data/answers.json') as stream:
        answers = json.load(stream)
        for answer in answers:
            if answer.get('user_id') == id and payload.get('question_id') == answer.get("question_id"):
                with open('data/alternatives.json') as stream:
                    alternatives = json.load(stream)
                    for alternative in alternatives:
                        if answer.get("question_id") == alternative.get('question_id'):
                            alternative['alternative'] = payload.get('answer')




















'''
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
'''