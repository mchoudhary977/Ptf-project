from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    PubDate = models.DateTimeField()
    Image = models.ImageField(upload_to='images/')
    Body = models.TextField()
