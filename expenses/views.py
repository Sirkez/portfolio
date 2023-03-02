from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Expenses
from .serializers import ExpensesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Show only user expenses
    def get_queryset(self):
        try:
            queryset = Expenses.objects.filter(owner = self.request.user)
            
        except:
            queryset = None
            return queryset
        
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains = name)
        description = self.request.query_params.get('description')
        if description:
            queryset = queryset.filter(description__icontains = description)
        amount_from = self.request.query_params.get('amount_from')
        if amount_from:
            queryset = queryset.filter(amount__gte = amount_from)
        amount_to = self.request.query_params.get('amount_to')
        if amount_to:
            queryset = queryset.filter(amount__lte = amount_to)
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__icontais = category)
        date_from = self.request.query_params.get('date_from')
        if date_from:
            queryset = queryset.filter(date__gte = date_from)
        date_to = self.request.query_params.get('date_to')
        if date_to:
            queryset = queryset.filter(date__lte = date_to)

        return queryset
        
    
    def list(self, request, *args, **kwargs):
        expenses = self.filter_queryset(self.get_queryset())
        expenses_count = expenses.count()
        serializer = ExpensesSerializer(expenses, many=True)
        response = {'expenses' : serializer.data, 'expenses_count':expenses_count, 'User':self.request.user.username}
        return Response(response)
