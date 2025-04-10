from django.urls import path
from .views import Index, Login, Signup, Dashboard,CreateTransaction, Logout, Deposit, Withdraw

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('createtransaction/', CreateTransaction.as_view(), name='createtransaction'),
    path('logout/', Logout.as_view(), name='logout'),
    path('deposit/', Deposit.as_view(), name='deposit'),
    path('withdraw/', Withdraw.as_view(), name='withdraw'),
]