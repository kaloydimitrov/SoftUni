# Generated by Django 4.1.7 on 2023-05-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_profile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]