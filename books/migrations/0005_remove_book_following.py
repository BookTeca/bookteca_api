# Generated by Django 4.1.7 on 2023-03-10 18:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_remove_following_book_title_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="following",
        ),
    ]
