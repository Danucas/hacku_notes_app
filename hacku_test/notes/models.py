from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)