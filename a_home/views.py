# from django.shortcuts import render

# def home_view(request):
#     return render(request, 'home.html')


from django.shortcuts import render
from a_plot.models import Plot  
from django.core.paginator import Paginator  # Import the Paginator class
from a_users.models import Profile



def home_view(request):
    plots = Plot.objects.all()
    level = Profile.objects.filter(level=request.user)
    
    paginator = Paginator(plots, 24)  # Show 24 plots per page
    page = int(request.GET.get('page', 1))
    plots = paginator.page(page)
    
    context = {
        'title': 'SuperCamper',
        'plots': plots,
        'level': level,
        'page': page,
    }
    return render(request, "index.html", context)