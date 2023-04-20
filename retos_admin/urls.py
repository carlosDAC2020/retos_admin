from django.contrib import admin
from django.urls import path
from . import views

app_name="retos_admin"

urlpatterns = [
        # login
    path('login/', views.login_admin, name="login"),
        # retos
    path('', views.index, name="index"),
    path('create_retos/', views.create_retos, name="create_retos"),
    path('retos_detail/', views.retos_detail, name="retos_detail"),

        # ----------- comunidades -------------------------
    path('comunidades/', views.comunidades, name="comunidades"),
    path('create_comunidades/', views.create_comunidades, name="create_comunidades"),
    path('comunidades_detail/', views.comunidades_detail, name="comunidades_detail"),

    # ----------- Instituciones -----------------------------------
    path('instituciones/', views.instituciones, name="instituciones"),
    path('create_instituciones/', views.create_instituciones, name="create_instituciones"),
    path('instituciones_detail/', views.instituciones_detail, name="instituciones_detail"),

    # ----------- espacios de co creacion -------------------------
    path('esp_co_creacion/', views.esp_co_creacion, name="esp_co_creacion"),
    path('create_esp_co_creacion/', views.create_esp_co_creacion, name="create_esp_co_creacion"),
    path('esp_co_creacion_detail/', views.esp_co_creacion_detail, name="esp_co_creacion_detail"),

    # ----------- Participantes -------------------------------------
    path('participantes/', views.participantes, name="participantes"),
    path('create_participantes/', views.create_participantes, name="create_participantes"),
    path('participantes_detail/', views.participantes_detail, name="participantes_detail"),
]