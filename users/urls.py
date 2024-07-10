from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.User_logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('deposit/', views.deposit_money, name='deposit_money'),
]
