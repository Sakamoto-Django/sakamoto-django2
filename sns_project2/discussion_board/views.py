from django.shortcuts import render

# Create your views here.
from django.views import generic


class DiscussionBoardView(generic.TemplateView):
    template_name = 'discussion.html'
