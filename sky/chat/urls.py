from django.urls import path
from . import views

app_name = 'chat'  # This is important for namespacing

urlpatterns = [
    path('', views.messages_page, name='messages_page'),  # URL pattern and name
]
