from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    personal_id = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name

    @property
    def get_username(self):
        return self.name
