from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),  # Index page
    path('home/', views.home, name="home"),  # Home page (restricted to authenticated users)
    path('login/', views.login_view, name="login"),  # Login page
    path('signup/', views.signup_view, name="signup"),  # Signup page
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
]
