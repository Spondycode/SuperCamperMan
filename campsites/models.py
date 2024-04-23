from django.db import models
import uuid
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Campsite(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    what3words = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    image1 = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    image2 = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    image3 = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    image4 = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    image5 = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    image6 = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contacted = models.BooleanField(default=False)
    contact_notes = models.TextField(blank=True, null=True)
    is_member = models.BooleanField(default=False)
    discount = models.BooleanField(default=False)
    num_plots = models.IntegerField(blank=True, null=True)
    list_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="campsites")
    site_id = models.CharField(max_length=100, default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-name"]
