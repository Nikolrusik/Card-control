from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin


class AbstractUserModel(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    username = models.CharField(
        verbose_name="Username", unique=True, max_length=24)
    email = models.EmailField(verbose_name="Email", unique=True)

    is_staff = models.BooleanField(
        verbose_name="staff status",
        default=False,
    )
    # is_superuser = models.BooleanField(
    #     verbose_name="Superuser status",
    #     default=False,
    #     help_text=_(
    #         "Designates whether the user can log into this admin site."
    #     ),
    # )
    EMAIL_FIELD = "username"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
