from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import InboxMessage, Conversation

# Create your views here.
@login_required
def inbox_view(request):
    context = {
        'conversation': 'conversation',
    }
    return render(request, 'a_inbox/inbox.html', context)