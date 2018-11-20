from django import forms
from .models import Todolist
class ToDoListForm(forms.ModelForm):
    class Meta:
        model=Todolist
        fields = (
            'title',
            'description',
            # 'date_time',
            'status',
            # 'created',
            # 'modified'
        )