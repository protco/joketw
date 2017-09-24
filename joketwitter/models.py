from django.db import models

# Create your models here.

class ContactUs(models.Model):
    """simple contact form"""
    contact_name = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=40)
    content = models.CharField(max_length=500, unique=True)

