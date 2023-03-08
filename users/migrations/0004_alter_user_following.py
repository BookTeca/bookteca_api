# Generated by Django 4.1.7 on 2023-03-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book_is_active"),
        ("users", "0003_alter_user_following"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="Following",
            field=models.ManyToManyField(related_name="user_book", to="books.book"),
        ),
    ]
