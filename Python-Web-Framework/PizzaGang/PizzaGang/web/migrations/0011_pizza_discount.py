# Generated by Django 4.1.7 on 2023-05-14 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
