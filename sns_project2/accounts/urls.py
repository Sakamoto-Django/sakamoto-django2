from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('create/', views.Create_account.as_view(), name='create'),
]
