from django.db import models

# Create your models here.
class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nim = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.content
