from pydantic import BaseModel, EmailStr
from typing import List




class Answer(BaseModel):
    question_id: int
    alternative_id: int


class UserAnswer(BaseModel):
    user_id: int
    answers: List[Answer]

class CreateUser(BaseModel):
    name: str
    mail: EmailStr
    phone: str

class DeleteUser(BaseModel):
    id: int

class UpdateUser(BaseModel):
    name: str
    mail: EmailStr
    phone: str

