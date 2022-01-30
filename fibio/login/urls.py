from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.client_login),
    path('worker/', views.worker_login)
]