from django.db import models

# Create your models here.
class UserItem(models.Model):
    item_number=models.IntegerField()
    item_name=models.CharField(max_length=30)
    item_quantity=models.IntegerField()
