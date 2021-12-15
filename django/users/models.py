from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserProfileManager
# Create your models here.


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = None
    phoneNo = models.CharField(max_length=12)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phoneNo']

    def __str__(self) -> str:
        return self.email
