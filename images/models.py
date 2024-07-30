from django.db import models

# Create your models here.
class Image(models.Model):
    pageURL = models.URLField()
    type = models.CharField(max_length=100)
    tags = models.TextField()
    webformatURL = models.URLField()
    views = models.IntegerField()
    downloads = models.IntegerField()
    likes = models.IntegerField()
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.type} - {self.tags} "