from django.urls import path, include
from rest_framework import routers

from .views import ExpensesViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('expenses', ExpensesViewSet)
router.register('categories', CategoryViewSet)

expenses_list = ExpensesViewSet.as_view({
    'get':'list',
    'post':'create'
})
expenses_detail = ExpensesViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})



urlpatterns = [
    path('', expenses_list, name='index'),
    path('<int:pk>/<str:name>', expenses_detail, name='expenses_detail')
]