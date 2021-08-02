from django.db import models


# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    prix = models.FloatField()
    remise = models.FloatField()
    categorie = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    adresse = models.CharField(max_length=1000)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
