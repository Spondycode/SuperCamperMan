from django.urls import path
from .views import campsite_list_view


urlpatterns = [
    path('', campsite_list_view, name="campsite-list"),
]