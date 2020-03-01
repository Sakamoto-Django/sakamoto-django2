from django.urls import path
from . import views

app_name = 'toppage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
]
