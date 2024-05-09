# Generated by Django 5.0.4 on 2024-05-09 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_delete_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="user",
            field=models.ForeignKey(
                limit_choices_to={"is_admin": False},
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("COMPLETED", "COMPLETED"),
                    ("PENDING", "PENDIENTE"),
                    ("DELAYED", "DELAYED"),
                ],
                default="PENDING",
                max_length=10,
            ),
        ),
    ]