from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout
from .models import UserProfile, Account
from .forms import SignupForm, LoginForm, DepositForm
from decimal import Decimal

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
        except UserProfile.DoesNotExist:
            return HttpResponse('Invalid credentials')

class Dashboard(View):
    def get(self, request):
        balance = 0
        return render(request, 'dashboard.html', {'balance': balance})
    
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

class Deposit(View):
    def get(self, request):
        depo_form = DepositForm()
        return render(request, 'deposit.html', {'form': depo_form})
    
    def post(self, request):
        form = DepositForm(request.POST)
        account = get_object_or_404(Account, account_number=Account.account_number, user_id=request.webapp.userprofile)

        if form.is_valid():
            amount = Decimal(form.cleaned_data['amount'])
            
        account.deposit(self, amount)
        return HttpResponse(f'Deposit of {amount} processed.')
    
class Withdraw(View):
    def get(self, request):
        return render(request, 'withdraw.html')
    
class Transfer(View):
    def get(self, request):
        return render(request, 'transfer.html')
    
    def post(self, request):
        sender_account = request.POST.get('sender_account')
        receiver_account = request.POST.get('receiver_account')
        amount = request.POST.get('amount')
        # Process transfer logic here
        return HttpResponse(f'Transfer of {amount} from {sender_account} to {receiver_account} processed.')
