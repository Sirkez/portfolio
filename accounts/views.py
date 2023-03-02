from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

from rest_framework.authtoken.models import Token

from .forms import CustomUserCreationForm


class RegisterCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:index')


    # Redirect authenticated user
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:index')
        return super(RegisterCreateView, self).dispatch(request, *args, **kwargs)


    # Login user after registration
    def form_valid(self, form):
        user = form.save()
        Token.objects.create(user = user)
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect(self.request.GET.get('next','accounts:index'))
  
        
        
class UserLoginView(LoginView):   
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    redirect_authenticated_user = True


    def get_succes_url(self):
         return redirect(self.request.GET.get('next','accounts:index'))


    


