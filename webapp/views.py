from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .forms import SignupForm, LoginForm
from .models import UserProfile

class Signup(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {'form': form}
        return render(request, 'signup.html', context)

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserProfile.objects.get(username=username, password=password)
            if user.password == password:
                return render(request, 'dashboard.html')
            else:
                return HttpResponse('Invalid credentials')
        except UserProfile.DoesNotExist:
            return HttpResponse('Invalid credentials')

class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')
    
class CreateTransaction(View):
    def get(self, request):
        return render(request, 'createtransaction.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserProfile.objects.get(username=username, password=password)
            if user.password == password:
                return render(request, 'dashboard.html')
            else:
                return HttpResponse('Invalid credentials')
        except UserProfile.DoesNotExist:
            return HttpResponse('Invalid credentials')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class Index(View):
    def get(self, request):
        return render(request, 'index.html')
