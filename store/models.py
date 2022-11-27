from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price= models.FloatField(default=0)
    description1 = models.CharField(null=True, max_length=200, blank=True)
    description2 = models.CharField(null=True, max_length=200, blank=True)
    description3 = models.CharField(null=True, max_length=200, blank=True)
    description4 = models.CharField(null=True, max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

        # if theirs no image function
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url