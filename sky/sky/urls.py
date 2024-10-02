from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Make sure to import settings
from django.conf.urls.static import static  # Import static to serve media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('griffin/', include('griffin.urls')),
    path('chat/', include('chat.urls', namespace='chat')),
]

# Serve media files during development
if settings.DEBUG:  # Ensure this is only active in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
