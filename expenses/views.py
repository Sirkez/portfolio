from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from collections import OrderedDict, defaultdict
from django.db.models.functions import Coalesce
from django.db.models import Sum, Value

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
        
        # Updating queryset with URL params
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
        if expenses:
            expenses_count = expenses.count()
            total_amount = expenses.aggregate(Sum('amount'))

            # Calculating summary per category from queryset
            summary_per_category = OrderedDict(sorted(
                expenses
                .annotate(category_name=Coalesce('category', Value('-')))
                .values('category_name')
                .annotate(s=Sum('amount'))
                .values_list('category_name', 's')))
            
            # Calculating summary per year and month from queryset
            summary_year_month =((
                expenses.values('date__year','date__month')
                .annotate(s=Sum('amount'))
                .order_by('-date__year','-date__month')
                .values_list('date__year','date__month','s')
                ))
            
            # Creating summary per year and month dict
            data = defaultdict(lambda: defaultdict(dict))
            for year, month, s in summary_year_month:
                data[year][month] = s

            serializer = ExpensesSerializer(expenses, many=True)
            response = {'expenses' : serializer.data,
                        'expenses_count': expenses_count,
                        'summary_per_category': summary_per_category,
                        'total_amount': total_amount,
                        'summary_per_year': data, 
                        'User': self.request.user.username}
            return Response(response)
            
        else:
            response = {'detail': 'No data provided'}
            return Response(response)
