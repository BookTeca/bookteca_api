from django.db import models


class StateOptions(models.TextChoices):
    NEW = "Novo"
    USED = "Usado"
    DAMAGE = "Danificado"


class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    is_available = models.BooleanField(default=True)
    state = models.CharField(max_length=10, choices=StateOptions.choices, default=StateOptions.NEW)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_copies",
    )
