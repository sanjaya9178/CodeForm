from django import forms
from .models import UserItem
from django.core import validators

class UserForm(forms.ModelForm):
    class Meta:
        model=UserItem
        fields=['item_number','item_name','item_quantity']
