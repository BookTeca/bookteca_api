# Generated by Django 4.1.7 on 2023-03-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("books", "0002_book_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Copy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_available", models.BooleanField(default=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Novo", "New"),
                            ("Usado", "Used"),
                            ("Danificado", "Damage"),
                        ],
                        default="Novo",
                        max_length=10,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book_copies",
                        to="books.book",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]