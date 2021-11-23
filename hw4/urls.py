from django.contrib import admin
from django.urls import path, include
import hw4.views

urlpatterns = [
    path('', hw4.views.index),
    path('tasks/', include('tasks.urls')),
]