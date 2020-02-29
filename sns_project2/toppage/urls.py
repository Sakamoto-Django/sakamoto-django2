from django.urls import path
from . import views

app_name = 'toppage'
urlnames = [
    path('', views.IndexView.as_view(), name='index')
]
