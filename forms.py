from django import forms
from .models import UserItem
from django.core import validators

class UserForm(forms.ModelForm):
    class Meta:
        model=UserItem
        fields=['item_number','item_name','item_quantity']

     with open('convert.txt', 'w') as convert_file:
        convert_file.write(json.dumps(dic))
    print_val=os.startfile('convert.txt', "print")

    return JsonResponse(print_val)
