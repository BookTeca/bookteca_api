# Generated by Django 4.1.7 on 2023-03-10 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("copies", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="copy",
            name="borrowings",
            field=models.ManyToManyField(
                related_name="borrowings_copy",
                through="copies.Borrowings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="borrowings",
            name="copy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="copy_borrowings",
                to="copies.copy",
            ),
        ),
        migrations.AddField(
            model_name="borrowings",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_copy_borrowings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
