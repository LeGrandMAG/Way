# Generated by Django 3.2.12 on 2022-04-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_course_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
