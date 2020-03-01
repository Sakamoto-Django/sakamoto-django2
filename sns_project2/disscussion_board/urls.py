from django.urls import path
from . import views

app_name = 'disscussion_board'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
