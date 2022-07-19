from django.db import models

# Create your models here.
"""post models."""
class User(models.Model):
    """user model"""
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100)

    firs_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank = True)

    birthdate = models.DateField(blank=True, null=True)

    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)