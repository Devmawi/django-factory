from django.db import models

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('created at')
    image = models.FileField('image', upload_to= './media/uploads')