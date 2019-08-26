from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/',  views.form_view, name='form_view'),
    path('list/', views.list_view, name='list_view'),
    path('edit/<int:list_id>/', views.delete_view, name='delete_view'),
    path('view/<int:view_id>/', views.todo_view, name='todo_view')
]
