from django.db import models


class StateOptions(models.TextChoices):
    NEW = "Novo"
    USED = "Usado"
    DAMAGE = "Danificado"


class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    is_available = models.BooleanField(null=True, default=True)
    state = models.CharField(max_length=10, choices=StateOptions.choices, default=StateOptions.NEW)

    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_copies",
    )

    users = models.ManyToManyField(
        "users.User",
        through="copies.Loan",
        related_name="borroweds_copies",
    )

    def __repr__(self):
        return f"<Copy [{self.id}] - Book [{self.book.id}]>"


class Loan(models.Model):
    class Meta:
        ordering = ["id"]

    loan_date = models.DateField(auto_now_add=True)
    estimated_return_date = models.DateField(null=True, default=None)
    return_date = models.DateField(null=True, default=None)
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="loans"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="borrowings_copies"
    )

    def __repr__(self):
        return f"<Loan [{self.id}]: User [{self.user.id}] - Copy [{self.copy.id}]>"
