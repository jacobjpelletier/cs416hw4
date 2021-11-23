from django import forms
from .models import Task


class TaskForm(forms.Form):
    task_item = forms.CharField(max_length=25,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Add tasks', 'name': 'task_item', 'type': 'text'}
                                ))
