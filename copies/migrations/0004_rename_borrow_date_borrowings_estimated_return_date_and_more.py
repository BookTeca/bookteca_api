# Generated by Django 4.1.7 on 2023-03-08 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0003_copy_borrowings"),
    ]

    operations = [
        migrations.RenameField(
            model_name="borrowings",
            old_name="borrow_date",
            new_name="estimated_return_date",
        ),
        migrations.RemoveField(
            model_name="borrowings",
            name="devolution_date",
        ),
        migrations.RemoveField(
            model_name="borrowings",
            name="estimated_devolution_date",
        ),
        migrations.AddField(
            model_name="borrowings",
            name="borrowing_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="borrowings",
            name="return_date",
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="copy",
            name="is_available",
            field=models.BooleanField(default=True, null=True),
        ),
    ]
