from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class LoginView(View):
    def get(self, request):
        context = {'form_mode': 'login'}
        return render(request, 'user_management/authenticate.html', context)
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'user_management/authenticate.html', {'form_mode': 'login'})


class RegisterView(View):
    def get(self, request):
        context = {'form_mode': 'register'}
        return render(request, 'user_management/authenticate.html', context)
    


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
    
@method_decorator(login_required(login_url='/user_management/login/'), name='dispatch')
class UserProfileView(View):
    def get(self, request):
        user_data = User.objects.filter(id=request.user.id).values()
        return render(request, "user_management/user_profile.html", {"user_data" : user_data})

    def post(self, request):
        user_data = User.objects.filter(id=request.user.id)
        return render(request, "user_management/user_profile.html", {"user_data" : user_data})