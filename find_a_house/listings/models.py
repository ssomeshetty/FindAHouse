from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/listings/', blank=True, null=True)  # Add ImageField

    def __str__(self):
        return self.title
