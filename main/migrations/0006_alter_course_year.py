# Generated by Django 3.2.12 on 2022-04-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220403_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.CharField(choices=[('All', 'All'), ('Freshman', '1'), ('Sophomore', '2'), ('Junior', '3'), ('Senior', '4')], max_length=100),
        ),
    ]