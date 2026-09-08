from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('tasks/create/', views.create_task),
    path('tasks/update/', views.update_task),
    path('login/', views.login),

]