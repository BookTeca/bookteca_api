# Generated by Django 4.1.7 on 2023-03-13 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("copies", "0001_initial"),
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="borrowings_copies",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="copy",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book_copies",
                to="books.book",
            ),
        ),
        migrations.AddField(
            model_name="copy",
            name="users",
            field=models.ManyToManyField(
                related_name="borroweds_copies",
                through="copies.Loan",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
