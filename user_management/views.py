from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models import F
from django.db.models.functions import Coalesce


class LoginView(View):
    def get(self, request):
        context = {"form_mode": "login"}
        return render(request, "user_management/authenticate.html", context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return render(
                request, "user_management/authenticate.html", {"form_mode": "login"}
            )


class RegisterView(View):
    def get(self, request):
        context = {"form_mode": "register"}
        return render(request, "user_management/authenticate.html", context)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        birth_date = request.POST.get("birth_date")

        print(f"username : {username} | email : {email} | password : {password}")

        user = User.objects.create_user(
            username=username, 
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(raw_password=password)
        user.save()

        UserProfile.objects.create(
            user=user,
            phone_number1=phone,
            address=address,
            birth_date=birth_date
        )
        login(request, user)
        return redirect("user_profile")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


@method_decorator(login_required(login_url="/user_management/login/"), name="dispatch")
class UserProfileView(View):
    def get(self, request):
        user_data = (
            User.objects.filter(id=request.user.id)
            .select_related("user_profile")
            .annotate(
                phone_number1=F("user_profile__phone_number1"),
                phone_number2=F("user_profile__phone_number2"),
                bio=F("user_profile__bio"),
                birth_date=F("user_profile__birth_date"),
                address=F("user_profile__address"),
            )
            .values()
            .first()
        )

        return render(
            request, "user_management/user_profile.html", {"user_data": user_data}
        )

    def post(self, request):

        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone1 = request.POST.get("phone1")
        phone2 = request.POST.get("phone2")
        address = request.POST.get("address")
        bio = request.POST.get("bio")
        birth_date = request.POST.get("birth_date")

        User.objects.filter(id=request.user.id).update(
            first_name=first_name, last_name=last_name, email=email, username=username
        )

        UserProfile.objects.update_or_create(
            user__id=request.user.id,
            defaults={
                "phone_number1": phone1,
                "phone_number2": phone2,
                "address": address,
                "bio": bio,
                "birth_date": birth_date,
            },
        )

        return redirect("user_profile")


class AccountView(View):
    def get(self, request):
        return render(request, "user_management/account.html")