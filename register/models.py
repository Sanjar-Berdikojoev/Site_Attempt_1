from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    ADMIN = 1
    Client = 2
    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (Client, 'Client')
    )

    MALE = 1
    FEMALE = 2
    GENDER_TYPE = (
        (MALE, 'MALE'),
        (FEMALE, "FEMALE"),
    )

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип Пользователя', default=Client)
    phone_number = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Гендер')

# Create your models here.
