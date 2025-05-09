# Generated by Django 5.2 on 2025-04-30 07:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="full_name",
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default-user.jpg",
                        null=True,
                        upload_to="user_folder",
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("about", models.TextField(blank=True, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
