from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('register', views.signupView, name='signup'),
    path('logout', views.logoutView, name='logout'),

    path('', views.home, name='home'),
]
