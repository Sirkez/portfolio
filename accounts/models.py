from django.db import models
from django.contrib.auth.models import AbstractUser
from marketplace.models import Auction

class CustomUser(AbstractUser):

    watchlist = models.ManyToManyField(Auction, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'