from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View

from authentication.forms import LoginForm, SignUpForm
from myuser.models import MyUser
# Create your views here.

class LoginView(View):
    form_class = LoginForm
    def get(self, request):
        form = self.form_class()
        return render(request, "generic_form.html", {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    

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

def custom_404(request):
    return render_to_response(404, RequestContext(request))

def custom_500(request):
    return render_to_response(500, RequestContext(request))
