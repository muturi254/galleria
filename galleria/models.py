from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.TextField(max_length=200)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('published at')
    image_url = models.ImageField(upload_to='images/%Y-%m-%d')

    def __str__(self):
        return self.image_name
