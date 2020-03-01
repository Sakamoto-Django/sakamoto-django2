from django.urls import path
from . import views

app_name = 'discussion_board'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]