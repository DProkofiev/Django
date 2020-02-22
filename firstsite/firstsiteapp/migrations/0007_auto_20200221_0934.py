# Generated by Django 3.0.3 on 2020-02-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstsiteapp', '0006_auto_20200221_0630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='links',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='link',
            field=models.URLField(default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
