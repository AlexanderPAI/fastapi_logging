import datetime


class AgeService:

    @staticmethod
    def get_age(birthdate: str):
        birthdate_datetime = datetime.datetime.strptime(birthdate, "%d.%m.%Y")
        now = datetime.datetime.now()
        return (now - birthdate_datetime).days // 356
