# Generated by Django 4.1.7 on 2023-03-12 02:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0005_remove_book_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="Following_book",
            field=models.ManyToManyField(
                related_name="Followings_books",
                through="books.Following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
