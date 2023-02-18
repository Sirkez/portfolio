from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

import datetime

class Category(models.Model):
    class Meta:
        ordering = ('-pk',)

    name = models.CharField(max_length=50, unique=True, default='Other')

    def __str__(self):
        return f'{self.name}'


class Auction(models.Model):

    class Meta:
        ordering = ('-date', '-pk')

    """CATEGORY = [
        ('am','Automotive'),
        ('re','Real Estate'),
        ('jb','Job'),
        ('hg','House and Garden'),
        ('ec','Electronics'),
        ('fa','Fashion'),
        ('sp','Sport'),
        ('ot','Other')
    ]"""
    
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    description = models.TextField(max_length=2000, blank=True)
    photo = models.ImageField(upload_to='marketplace/', blank=True, default='/blank/blank.jpg')
    created_by = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, db_index=True)
    slug = models.SlugField(max_length=200)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Auction, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('marketplace:auction', args=[str(self.pk), str(self.slug)])


    def __str__(self):
        return f'{self.name}-{self.pk}'