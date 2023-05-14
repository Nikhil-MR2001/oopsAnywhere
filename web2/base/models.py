from django.db import models


# Create your models here.
class farm(models.Model):
    img = models.ImageField(null=True)
    head = models.CharField(max_length=300, null=True)
    body = models.CharField(max_length=300, null=True)


