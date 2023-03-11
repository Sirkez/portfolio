from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/index.html'), name='index'),
    path('create/', views.create_post, name='create'),
    path('update/<slug:slug>/', views.update_post, name='update')
]