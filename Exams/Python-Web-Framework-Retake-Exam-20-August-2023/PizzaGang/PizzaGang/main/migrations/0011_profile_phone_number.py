# Generated by Django 4.1.7 on 2023-07-18 21:04

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_cartitem_created_at_cartitem_is_half_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
