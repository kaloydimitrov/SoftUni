# Generated by Django 4.1.4 on 2022-12-21 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
