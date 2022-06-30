import re
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    id: int
    title: str
    price: float
    is_trending: bool

app = FastAPI()

fakeDB = []

@app.get("/")
def index():
    return {"Welcome": "Simple Course API"}

@app.get("/courses/")
def get_courses():
    return fakeDB

@app.get("/courses/{id}")
def get_course_from_id(id:int):
    return fakeDB[id-1]

@app.post("/courses/")
def add_course(request: Course):
    fakeDB.append(request.dict())
    return request

@app.delete("/courses/{id}")
def delete_course(id:int):
    fakeDB.pop(id-1)
    return {"Message": "Course Deletion Successful"}