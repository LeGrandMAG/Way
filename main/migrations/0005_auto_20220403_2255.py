# Generated by Django 3.2.12 on 2022-04-03 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220401_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='topic',
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.topic'),
        ),
    ]
