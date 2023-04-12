from django.contrib import admin
from django.urls import path
from . import views

app_name="retos_admin"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_admin, name="login"),
]