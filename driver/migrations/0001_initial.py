# Generated by Django 4.2 on 2024-09-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("personal_id", models.CharField(max_length=11, unique=True)),
                ("license_number", models.CharField(max_length=20, unique=True)),
                ("phone_number", models.CharField(blank=True, max_length=15, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
