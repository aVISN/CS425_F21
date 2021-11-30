from django.db import models

# Create your models here.

class Upload(models.Model):
    description = models.CharField(max_length=100)
    comments = models.TextField(blank=True)
    filename = models.FileField(upload_to='')

    def __str__(self):
        return self.description
