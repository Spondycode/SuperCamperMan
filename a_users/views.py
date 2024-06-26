from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from a_plot.views import Plot
from django.contrib import messages
from a_inbox.forms import InboxNewMessageForm
from .forms import *
from a_plot.models import Plot
from django.core.paginator import Paginator
from django.http import Http404

# # PROFILE VIEW 1
# @login_required
# def profile_view(request, username=None):
#     if username:
#         profile = get_object_or_404(User, username=username).profile
#     else:
#         try:
#             profile = request.user.profile
#         except:
#             return redirect('account_login')
        
#     new_message_form = InboxNewMessageForm()
    
#     context = {
#         'profile':profile,
#         'new_message_form':new_message_form
#     }
#     return render(request, 'a_users/profile.html', context)




# PROFILE VIEW 2 -  View the profile of the logged in user and show plots created by the user
def profile_view(request, username=None):
    if request.user.is_authenticated:
        
        plots = Plot.objects.filter(owner=request.user)  # Fetch plots created by the logged in user
        profile = request.user.profile
        
        paginator = Paginator(plots, 24)  # Show 12 plots per page
        page = int(request.GET.get('page', 1))
        plots = paginator.page(page)
        
        context = {
            "profile": profile,
            "plots": plots,
            'page': page,
            
        }
        return render(request, "a_users/profile.html", context)
    else:
        messages.success(request, "You need to login first")
        return redirect("/login")



# View the profile of an owner os a plot and show plots created by the user
def user_profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        plots = Plot.objects.filter(owner=user)  # Fetch plots created by the logged in user
        profile = user.profile
        
        paginator = Paginator(plots, 24)  # Show 12 plots per page
        page = int(request.GET.get('page', 1))
        plots = paginator.page(page)
        
        new_message_form = InboxNewMessageForm() # form to send a message to the user from the profile page
        
        context = {
            "plots": plots,
            "profile": profile,
            "new_message_form": new_message_form,
            "page": page,
        }
        return render(request, "a_users/user_profile.html", context)
    except User.DoesNotExist:
        raise ("User does not exist")
    except Plot.DoesNotExist:
        raise Http404("Plot does not exist")




@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            
            if request.user.emailaddress_set.get(primary=True).verified:
                return redirect('profile')
            else:
                return redirect('profile-verify-email')
        
    if request.path == reverse("profile-onboarding"):
        template = 'a_users/profile_onboarding.html'
    else:
        template = 'a_users/profile_edit.html'
        
    return render(request, template, {"form": form})










@login_required
def profile_settings_view(request):
    return render(request, 'a_users/profile_settings.html')


@login_required
def profile_emailchange(request):
    
    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form':form})
    
    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)

        if form.is_valid():
            
            # Check if the email already exists
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')
            
            form.save() 
            
            # Then Signal updates emailaddress and set verified to False
            
            # Then send confirmation email 
            send_email_confirmation(request, request.user)
            
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Form not valid')
            return redirect('profile-settings')
        
    return redirect('home')


@login_required
def profile_emailverify(request):
    send_email_confirmation(request, request.user)
    return redirect('profile-settings')


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('home')
    
    return render(request, 'a_users/profile_delete.html')


def profile_verify_email(request):
    send_email_confirmation(request, request.user)
    return redirect('profile')