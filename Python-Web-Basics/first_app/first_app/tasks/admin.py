from django.contrib import admin
from first_app.tasks.models import Task

admin.site.register(Task)
