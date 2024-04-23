from django.shortcuts import render

from .models import Campsite

def campsite_list_view(request):
    campsites = Campsite.objects.all()
    return render(request, 'campsites/campsite_list.html', {'campsites': campsites})
