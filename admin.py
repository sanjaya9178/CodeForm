from django.contrib import admin
from .models import UserItem
# Register your models here.

@admin.register(UserItem)
class UserAdmin(admin.ModelAdmin):
    list_display = ('item_number','item_name','item_quantity')
