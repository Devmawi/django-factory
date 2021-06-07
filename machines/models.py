from django.db import models

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    image = models.FileField('image', upload_to= './media/uploads')

class Product(models.Model):
    name = models.CharField(max_length=200)