from django.contrib import admin
from .models import InboxMessage, Conversation

class InboxMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('sender', 'conversation', 'body')
    

admin.site.register(InboxMessage, InboxMessageAdmin)
admin.site.register(Conversation)


