# Generated by Django 4.1.7 on 2023-03-10 13:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BookFollowing",
            new_name="Following",
        ),
    ]