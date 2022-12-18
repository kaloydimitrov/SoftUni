# Generated by Django 4.1.4 on 2022-12-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_employees_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='level',
            field=models.IntegerField(choices=[(0, 'Trainee'), (1, 'Junior'), (2, 'Middle'), (3, 'Senior')], default='Trainee'),
        ),
    ]