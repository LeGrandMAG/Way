# Generated by Django 3.2.12 on 2022-04-23 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_course_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='course',
            name='current_students',
        ),
        migrations.AddField(
            model_name='course',
            name='current_students',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.topic'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]