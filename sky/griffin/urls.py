from django.urls import path
from . import views  # Import all views from the current directory

urlpatterns = [
    path('', views.list_projects, name='list_projects'),  # Redirect root to list_projects
    path('create/', views.create_project, name='create_project'),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
]
