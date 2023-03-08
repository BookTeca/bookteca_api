from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_blocked = models.BooleanField(default=False)

    Following = models.ManyToManyField(
        "books.Book",
        related_name="user_book"
    )
