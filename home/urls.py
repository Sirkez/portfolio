from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create_post, name='create'),
    path('update/<slug:slug>/', views.update_post, name='update'),
    path('delete/<slug:slug>/', views.delete_post, name='delete'),
    path('post/<slug:slug>', views.post, name='post')
]