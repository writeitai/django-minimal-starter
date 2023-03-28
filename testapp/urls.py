from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('list', views.TaskListView.as_view(), name='task-list'),
]
