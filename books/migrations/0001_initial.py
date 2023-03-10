# Generated by Django 4.1.7 on 2023-03-13 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(null=True)),
                ("author", models.CharField(max_length=255)),
                ("published_date", models.DateField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Drama", "Drama"),
                            ("Tecnologia", "Tecnologia"),
                            ("Mangá", "Manga"),
                            ("Aventura", "Aventura"),
                            ("Policial", "Policial"),
                            ("Not Informed", "Default"),
                        ],
                        default="Not Informed",
                        max_length=100,
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Following",
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
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book_following",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]
