from django.db import models
from django.template.defaultfilters import slugify

from accounts.models import CustomUser
from .utils import unique_slugify

import datetime

class Expenses(models.Model):
    class Meta:
        ordering = ('-date','-pk')

    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=16)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(default=datetime.date.today, db_index=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, null = True)

    # Saving unique slug
    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(Expenses, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    



