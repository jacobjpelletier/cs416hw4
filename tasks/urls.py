from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tasks, name='view_tasks'),
    path('add_task', views.add_task, name='add_task'),
]