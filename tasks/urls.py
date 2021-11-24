from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_tasks, name='view_tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
    path('update/<int:id>', views.update_task, name='update_task'),
    path('complete/<int:id>', views.complete_task, name='complete_task'),
]