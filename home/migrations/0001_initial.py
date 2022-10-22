# Generated by Django 4.1.2 on 2022-10-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                ("business_id", models.CharField(max_length=84)),
                ("username", models.CharField(max_length=84)),
                ("image_url", models.CharField(max_length=100, null=True)),
                ("review_text", models.TextField()),
                ("timestamp", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "image",
                    models.ImageField(
                        blank=True, default="avatar.png", null=True, upload_to=""
                    ),
                ),
                ("city", models.CharField(default="", max_length=84, null=True)),
                ("mobile", models.CharField(default="", max_length=84, null=True)),
                (
                    "username",
                    models.CharField(max_length=83, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]
