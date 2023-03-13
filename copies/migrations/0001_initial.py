# Generated by Django 4.1.7 on 2023-03-13 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

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
                ("is_available", models.BooleanField(default=True, null=True)),
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
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Loan",
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
                ("loan_date", models.DateField(auto_now_add=True)),
                ("estimated_return_date", models.DateField(default=None, null=True)),
                ("return_date", models.DateField(default=None, null=True)),
                (
                    "copy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loans",
                        to="copies.copy",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
