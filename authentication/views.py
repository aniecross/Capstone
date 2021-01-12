from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View
from django.http import HttpResponse

from authentication.forms import LoginForm, SignUpForm
from myuser.models import MyUser

from django.contrib import messages
# Create your views here.

class LoginView(View):
    form_class = LoginForm
    def get(self, request):
        form = self.form_class()
        return render(request, "generic_form.html", {'form': form, 'errors': None})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
            else:
                return render(request, "generic_form.html", {'form': form, 'errors':'Invalid username or password'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('homepage'))


class SignUpView(View):
    form_class = SignUpForm
    def get(self, request):
        form = self.form_class()
        return render(request, 'generic_form.html', {'form': form})
        
    def post(self, request):    
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                username=data['username'], password=data['password'], email=data['email'],
                first_name=data['first_name'], last_name=data['last_name']
            )
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


def page_not_found(request, exception):

    return render(request, '404.html', {})

def internal_server_error(request):

    return render(request, '500.html', {})
