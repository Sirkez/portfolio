from django.db import models
from django.template.defaultfilters import slugify

from accounts.models import CustomUser

import datetime

class Expenses(models.Model):
    class Meta:
        ordering = ('-date','-pk')

    name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=16)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateField(auto_now_add=True, db_index=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, null = True)

    # Saving unique slug
    def save(self):
        if self.slug == None:
            slug = slugify(self.name)

            has_slug = Expenses.objects.filter(slug=slug).exists()
            count = 0
            while has_slug:
                count += 1
                slug = slugify(self.name) + '-' + str(count)
                has_slug = Expenses.objects.filter(slug=slug).exists()

            self.slug = slug  
        super().save()     


    def __str__(self):
        return self.name
    



