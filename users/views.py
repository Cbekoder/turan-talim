from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.views import View


class LoginRegisterView(View):
    def get(self, request):
        return render(request, 'login_register.html')

    def post(self, request):
        type_post = request.POST.get('form_type')

        if type_post == 'login':
            login_email_or_phone = request.POST.get('login')
            password = request.POST.get('password')

            user = authenticate(request, username=login_email_or_phone, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('/')  # Redirect to a logged-in homepage
            else:
                messages.error(request, "Invalid login credentials")
                return redirect('signing')

        elif type_post == 'register':
            first_name = request.POST.get('first_name')
            login_email_or_phone = request.POST.get('login')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('signing')

            if User.objects.filter(username=login_email_or_phone).exists():
                messages.error(request, "User with this email or phone already exists")
                return redirect('singing')

            user = User.objects.create_user(username=login_email_or_phone, password=password)
            user.first_name = first_name
            user.save()

            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('/')

        return redirect('signing')

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


def logoutView(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/')
