from django.shortcuts import render
from rest_framework import viewsets

from .models import Expenses, Category
from .serializers import ExpensesSerializer, CategorySerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        try:
            queryset = Expenses.objects.filter(owner = self.request.user)
            return queryset
        except:
            queryset = None
            return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

