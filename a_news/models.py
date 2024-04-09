from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    intro = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
