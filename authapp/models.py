from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class AbstractUserModel(AbstractBaseUser):
    email = models.EmailField(verbose_name="Username/Email", unique=True)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
