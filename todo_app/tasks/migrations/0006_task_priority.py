# Generated by Django 5.0.4 on 2024-05-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_alter_task_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]