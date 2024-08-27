from datetime import datetime
from pydantic import BaseModel


class BirthdateModel(BaseModel):
    birthdate: datetime


class PersonModel(BaseModel):

    first_name: str
    last_name: str
    birthdate: BirthdateModel
