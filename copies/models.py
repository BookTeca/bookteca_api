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
    borrowings = models.ManyToManyField(
        "users.User",
        through="copies.Borrowings",
        related_name="borrowings_copy"
    )


class Borrowings(models.Model):
    class Meta:
        ordering = ["id"]

    borrow_date = models.DateField()
    estimated_devolution_date = models.DateTimeField()
    devolution_date = models.DateTimeField(auto_now=True)
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="copy_borrowings"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_copy_borrowings"
    )
