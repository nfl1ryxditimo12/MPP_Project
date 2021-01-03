from django.urls import path

from soogle import views

urlpatterns = [
    path('', views.index),
    path('page1', views.page1, name='page1'),
]
