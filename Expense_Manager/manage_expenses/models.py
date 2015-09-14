from django.db import models

# Model to store expense for a particular user
# expense_poster : The Person who recorderd/made the purchase
# username : User who is liable to pay for the purchase
# cost : The amount payable by the user
# description : A short description about the purchase
# purchase_date : Date of purchase "Empty as of the current state"
# purchase_store : The place where the purchase was made
class UserExpense(models.Model):
    expense_poster= models.CharField(max_length=200, default="") # the person who updated the expense
    username = models.CharField(max_length=200, default = "") #whose
    cost = models.FloatField(default = 0) #how much
    description = models.CharField(max_length=200, default="") #what
    purchase_date = models.CharField(max_length=100) #when
    purchase_store = models.CharField(max_length=100) #where
    
    def __str__(self):
        return self.username