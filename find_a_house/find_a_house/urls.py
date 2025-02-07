from django.contrib import admin
from django.urls import path
from listings.views import listing_list, listing_retreve, listing_create, listing_update
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list, name='listing_list'),
    path('listings/<int:pk>/', listing_retreve, name='listing_retreve'),
    path('add-listing/', listing_create, name='listing_create'),
    path('listings/<int:pk>/edit/', listing_update, name='listing_update'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
