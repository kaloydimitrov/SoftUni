# Generated by Django 4.1.7 on 2023-05-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_pizza_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]