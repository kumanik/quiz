from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audio/', blank=True)
