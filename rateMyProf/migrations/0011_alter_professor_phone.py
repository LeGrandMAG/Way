# Generated by Django 3.2.12 on 2022-04-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateMyProf', '0010_professor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='phone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
