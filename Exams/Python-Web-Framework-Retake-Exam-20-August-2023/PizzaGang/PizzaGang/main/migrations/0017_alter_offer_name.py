# Generated by Django 4.1.7 on 2023-07-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_offer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
