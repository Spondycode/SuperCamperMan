"""
URL configuration for a_core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view, user_profile_view
from a_home.views import *

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('bossman/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name="home"),
    path('profile/', include('a_users.urls')),
    path("", include("a_plot.urls")),
    path('inbox/', include("a_inbox.urls")),
    path('@<username>/', profile_view, name="profile"),
    path('<username>/', user_profile_view, name="user-profile"),
]

# Only used in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
