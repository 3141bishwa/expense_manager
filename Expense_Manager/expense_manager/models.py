from django.db import models

class UserExpense(models.Model):
    expense_poster= models.CharField(max_length=200, default="") # the person who updated the expense
    username = models.CharField(max_length=200, default = "") #whose
    cost = models.FloatField(default = 0) #how much
    description = models.CharField(max_length=200, default="") #what
    purchase_date = models.CharField(max_length=100) #when
    purchase_store = models.CharField(max_length=100) #where
    
    def __str__(self):
        return self.username