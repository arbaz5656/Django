from django.db import models

# Create your models here.

class Todoadd(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title