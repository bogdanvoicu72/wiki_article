from django.db import models

# Create your models here.

class Document(models.Model):
    desc = models.CharField(max_length=50)
    document = models.ImageField(upload_to='image/')
