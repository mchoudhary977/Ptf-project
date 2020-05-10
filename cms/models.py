from django.db import models

class Certificate(models.Model):
    CertificateBadge = models.ImageField(upload_to='images/')
    CertificateImage = models.ImageField(upload_to='images/')
    Title = models.CharField(max_length=200)
    CertificationDate = models.DateTimeField()

    def __str__(self):
        return self.Title
