from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('applyPage/', views.applyPage, name="applyPage"),
    path('confirmPage/', views.confirmPage, name="confirmPage"),
]