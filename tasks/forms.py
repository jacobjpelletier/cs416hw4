from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # (2)
        fields = '__all__'  # use all table columns (fields)