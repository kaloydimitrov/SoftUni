# Generated by Django 4.1.4 on 2022-12-17 18:59

from django.db import migrations, models
import forms_two.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_person_age_alter_person_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(error_messages={'unique': 'The name is already taken'}, max_length=22, unique=True, validators=[forms_two.web.validators.is_upper]),
        ),
    ]
