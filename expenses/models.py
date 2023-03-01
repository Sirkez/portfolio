from django.db import models
from accounts.models import CustomUser

import datetime

class Category(models.Model):
    class Meta:
        ordering = ('-name', '-pk')

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Expenses(models.Model):
    class Meta:
        ordering = ('-date','-pk')

    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=16)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(default=datetime.date.today, db_index=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


