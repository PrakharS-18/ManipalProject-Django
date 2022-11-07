from django.db import models

# making database dynamic for products

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/')

    # to display name not like product object 1 or 2
    # this is default function we need to override it
    def __str__(self):
        return self.title
