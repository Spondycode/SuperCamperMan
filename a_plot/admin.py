from django.contrib import admin
from .models import Plot, Comment, Reply, LikedPlot, LikedComment, Campsite


admin.site.register(Plot)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPlot)
admin.site.register(LikedComment)
admin.site.register(Campsite)