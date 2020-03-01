from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login. authenticate
from django.views.generic import CreateView
from .forms import UserCreateForm

# Create your views here.
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form=UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #read "username" from from
            username=form.cleaned_data.get('usename')
            #read "password1" from form
            password1=form.cleaned_data.get('password1')
