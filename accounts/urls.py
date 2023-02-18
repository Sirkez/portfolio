from django.urls import path, reverse_lazy
from django.views.generic import CreateView, TemplateView

from .models import CustomUser
from .forms import UserCreationForm
from .views import RegisterCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'accounts/index.html'), name='index'),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('logout/', UserLogoutView.as_view(), name='logout')
]