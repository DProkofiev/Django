# Generated by Django 3.0.3 on 2020-02-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstsiteapp', '0004_year_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='update',
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
