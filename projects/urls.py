from django.urls import path

from .import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create/', views.create_project, name='create-project'),
    path('edit/<str:pk>/', views.edit_project, name='edit-project'),
    path('delete/<str:pk>/', views.delete_project, name='delete-project'),
]
