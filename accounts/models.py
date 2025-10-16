from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    google_id = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.email
