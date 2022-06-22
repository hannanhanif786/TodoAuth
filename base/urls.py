from django.urls import path
from . import views
urlpatterns = [
    path("list", views.TaskList.as_view()),
    path("create", views.TaskList.as_view()),
    path("retrieve/<pk>", views.TaskDetail.as_view()),
    path("update/<pk>", views.TaskDetail.as_view()),
    path("delete/<pk>", views.TaskDetail.as_view()),
]
