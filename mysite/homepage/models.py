from django.db import models
from django.contrib import admin

# Create your models here.
# Creates entries in db

# class Home(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
        
#     def __str__(self):
#         return self.title
    
class Purchase(models.Model):
    store = models.CharField(max_length=100)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    products = models.TextField()
    
    
    def __str__(self):
        return f'{self.store} - {self.amount_spent} on {self.purchase_date}'

    