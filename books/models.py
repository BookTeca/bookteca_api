from django.db import models

class CategoryBook(models.TextChoices):
    DRAMA = "Drama"
    TECNOLOGIA = "Tecnologia"
    MANGA = "Mangá"
    AVENTURA = "Aventura"
    POLICIAL = "Policial"
    DEFAULT = "Not Informed"

class Book(models.Model):

    class Meta:
        ordering = ("id",)
    
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    category = models.CharField(max_length=100, choices=CategoryBook.choices, default=CategoryBook.DEFAULT)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    following = models.ManyToManyField(
        "users.User",
        through="books.BookFollowing",
        related_name="following_books"
    )

class BookFollowing(models.Model):
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_following"
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_book_following"
    )
