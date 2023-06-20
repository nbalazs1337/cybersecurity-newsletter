from django.db import models

# Create your models here.

class FeedlyItem(models.Model):
    title = models.CharField(max_length=200)


class Recipient(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email
    
class NewDisclosure(models.Model):
    cve = models.CharField(max_length=20)
    issue = models.CharField(max_length=200)
    link = models.URLField()



