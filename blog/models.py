from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    PubDate = models.DateTimeField()
    Image = models.ImageField(upload_to='images/')
    Body = models.TextField()

    def __str__(self):
        return self.Title

    def summary(self):
        return self.Body[:100]

    def pub_date_pretty(self):
        return self.PubDate.strftime('%b %e %Y')
