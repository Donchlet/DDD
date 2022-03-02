from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class CustomUser(User):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )
    OCUP_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
        ("MILLIONAIRE", "MILLIONAIRE")
    )
    phone_number = models.CharField("phone_number", max_length=60, unique=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")
    age = models.IntegerField()
    occupation = models.CharField(choices=OCUP_CHOICE, max_length=80)
    mothers_maiden_name = models.CharField(max_length=60)
    best_friend_name = models.CharField(max_length=70)
    place_of_residence = models.CharField(max_length=30)
    favorite_song = models.CharField(max_length=50)
    first_book = models.CharField(max_length=45)