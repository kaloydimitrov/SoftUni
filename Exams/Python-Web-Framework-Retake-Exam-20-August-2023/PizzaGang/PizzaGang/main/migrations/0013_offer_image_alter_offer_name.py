# Generated by Django 4.1.7 on 2023-07-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_offer_alter_cartitem_final_price_alter_pizza_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]