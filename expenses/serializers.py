from rest_framework import serializers

from .models import Expenses

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        exclude = ('owner','slug')
