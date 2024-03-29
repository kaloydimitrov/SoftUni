# Generated by Django 4.1.4 on 2022-12-10 13:40

from django.db import migrations
from django.utils.text import slugify


def add_slugs(apps, schema_editor):
    Departments = apps.get_model('web', 'Departments')
    deps = Departments.objects.all()

    for dep in deps:
        dep.slug = slugify(dep.name)

    Departments.objects.bulk_update(deps, ['slug'])


def delete_slugs(apps, schema_editor):
    Departments = apps.get_model('web', 'Departments')
    deps = Departments.objects.all()

    for dep in deps:
        dep.slug = None

    Departments.objects.bulk_update(deps, ['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_alter_departments_options_alter_employees_options_and_more'),
    ]

    operations = [
        migrations.RunPython(add_slugs, delete_slugs),
    ]
