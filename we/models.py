from django.db import models

# Create your models here.

class WorkExp(models.Model):
    OraganizationName = models.CharField(max_length=255)
    ProjectTitle = models.CharField(max_length=255)
    FromDate = models.DateTimeField()
    toDate = models.DateTimeField()
    Client = models.CharField(max_length=255)
    Role = models.CharField(max_length=255)
    Decription = models.TextField()
    Responsibilities = models.TextField()
    Environments = models.CharField(max_length=255)
    ProjectLogo = models.ImageField(upload_to='images/')
