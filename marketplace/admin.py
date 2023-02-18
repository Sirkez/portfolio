from django.contrib import admin

from .models import Auction, Category
# Register your models here.

class AuctionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Category)