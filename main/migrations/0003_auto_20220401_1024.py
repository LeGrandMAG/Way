# Generated by Django 3.2.12 on 2022-04-01 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_professor_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='topic',
        ),
        migrations.AddField(
            model_name='topic',
            name='department',
            field=models.BooleanField(default=True),
        ),
    ]
