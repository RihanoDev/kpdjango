from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Addusers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)  
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
