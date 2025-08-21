from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):
    name: str = 'Jawad'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4, default=3.9 , description = 'A desimal value representing the result of the student')

new_student = {'age': 27, 'cgpa': 2.9, 'email': 'jawad@gmail.com'}

student = Person(**new_student)

print(student.name)
print(student.age)