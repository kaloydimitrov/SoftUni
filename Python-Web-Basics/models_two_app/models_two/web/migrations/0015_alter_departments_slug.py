# Generated by Django 4.1.4 on 2022-12-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_fill_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
