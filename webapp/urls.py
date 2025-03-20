from django.urls import path
from .views import Index, Login, Signup, Dashboard

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]