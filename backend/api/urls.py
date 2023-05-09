from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/create/', views.TodoListCreate.as_view()),
    path('todos/update/<pk>', views.TodoUpdate.as_view()),
    path('todos/delete/<pk>', views.TodoDelete.as_view()),
    path('todos/<pk>/complete/', views.TodoToggleComplete.as_view()),
]
