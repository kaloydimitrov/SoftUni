from django.contrib import admin

from models_demo.web_demo.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
