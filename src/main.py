import logging
import datetime
from fastapi import FastAPI

from src.schemes.person import BirthdateModel
from src.utils.age_service import AgeService

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello!"
    }


@app.post(
    "/get_age",
)
async def get_age(birthdate: str):
    age_service = AgeService()
    age = age_service.get_age(birthdate)
    return {
        "age": age
    }
