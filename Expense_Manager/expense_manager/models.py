from django.db import models
from django.contrib.auth.models import User

class UserExpense(models.Model):
    user = models.ForeignKey(User) #whose
    cost = models.FloatField(default = 0) #how much
    description = models.CharField(max_length=200, default="") #what
    purchase_date = models.CharField(max_length=100) #when
    purchase_store = models.CharField(max_length=100) #where
    
    def __str__(self):
        return self.user.username