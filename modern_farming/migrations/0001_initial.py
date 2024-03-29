# Generated by Django 4.1.5 on 2023-01-21 06:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("crop_type", models.CharField(max_length=50)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name_plural": "Categories",},
        ),
        migrations.CreateModel(
            name="ModernFarming",
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
                ("tech_name", models.CharField(max_length=100)),
                (
                    "video",
                    models.FileField(
                        upload_to="modern_farming/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
                            )
                        ],
                    ),
                ),
                ("process", models.TextField(max_length=2000)),
                ("required_tool", models.TextField(max_length=500)),
                ("soil_report", models.TextField(max_length=500)),
                ("season", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="modern_farming.category",
                    ),
                ),
            ],
            options={"ordering": ["-created"],},
        ),
    ]
