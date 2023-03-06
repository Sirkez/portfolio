from django.contrib import admin

from .models import Expenses

class ExpensesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Expenses, ExpensesAdmin)
