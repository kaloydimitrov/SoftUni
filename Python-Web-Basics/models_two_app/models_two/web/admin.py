from django.contrib import admin
from models_two.web.models import Employees, Departments, Projects


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Employees)


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Departments)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass
