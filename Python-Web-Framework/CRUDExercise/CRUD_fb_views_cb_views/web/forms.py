from django import forms
from CRUD_fb_views_cb_views.web.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description')
