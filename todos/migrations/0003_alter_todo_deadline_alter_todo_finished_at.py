# Generated by Django 4.2.1 on 2024-03-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_alter_todo_finished_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateField(blank=True, null=True),
        ),
    ]
