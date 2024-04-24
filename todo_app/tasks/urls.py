from django.shortcuts import path;

from . import views

urlpatterns = [
    path("tasks_list", views.tasks_list, name="tasks_list"),
    path("users", views.users_list, name="users_list")
]
