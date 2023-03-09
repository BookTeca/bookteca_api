from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta:
        ordering = ["username"]
        db_table = "User"
        unique_together = ["username", "email"]

    is_blocked = models.BooleanField(default=False)
    email = models.EmailField(
        max_length=200,
        unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


