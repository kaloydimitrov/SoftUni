# Generated by Django 4.1.7 on 2023-07-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_pizza_duplication_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='is_big',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_large',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='is_small',
            field=models.BooleanField(default=False),
        ),
    ]
