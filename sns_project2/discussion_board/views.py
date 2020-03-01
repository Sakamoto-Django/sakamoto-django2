from django.shortcuts import render

# Create your views here.
import datetime


def DiscussionBoardView(request):
    return render(request, 'discussion.html')
