from django.shortcuts import render

from . import models
# Create your views here.
from django.views.generic import ListView, TemplateView
from .models import Task


class HomePageView(TemplateView):
    model = Task
    template_name = 'home.html'

class TaskListView(ListView):
    model = Task
    template_name = 'task/list.html'
   

