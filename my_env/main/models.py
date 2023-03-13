from django.db import models

# Create your models here.

class FeedlyItem(models.Model):
    title = models.CharField(max_length=200)
