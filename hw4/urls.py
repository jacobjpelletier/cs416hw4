from django.contrib import admin
from django.urls import path, include
import hw4.views
import tasks.views

urlpatterns = [
    path('', tasks.views.view_tasks),
    path('tasks/', include('tasks.urls')),
]