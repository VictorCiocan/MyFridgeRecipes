from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

class LoginUserView(LoginView):
    template_name = "authentication/form.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home-page')

class RegisterPage(FormView):
    template_name = "authentication/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home-page')
        return super(RegisterPage, self).get(*args, **kwargs)

class UserChangePasswordView(PasswordChangeView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('home-page')



# class LogoutUserView(LogoutView):
#     success_url = reverse_lazy('home-page')




