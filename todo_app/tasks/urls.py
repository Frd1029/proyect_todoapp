from django.urls import path;

from . import views

urlpatterns = [
    path("tasks", views.tasks_list, name="tasks_list"),
    path("users", views.users_list, name="users_list")
]
