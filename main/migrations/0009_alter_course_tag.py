# Generated by Django 3.2.12 on 2022-04-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_course_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
