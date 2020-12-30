from django.urls import path

from soogle import views

urlpatterns = [
    path('', views.index),
]