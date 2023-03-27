from django.contrib import admin

from skill_test_app.web.models import User


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    pass
