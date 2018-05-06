from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

     # save method
    def location_save(self):
        self.save()
    # delete method
    def location_delete(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

     # save method
    def category_save(self):
        self.save()
    # delete method
    def category_delete(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(category_name=value)


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.TextField(max_length=200)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('published at', auto_now_add=True)
    image_url = models.ImageField(upload_to='images/%Y-%m-%d', null=True)

    def __str__(self):
        return self.image_name 

    # save method
    def image_save(self):
        self.save()
    # delete method
    def image_delete(self):
        self.delete()

    @classmethod
    def get_image_by_Id(cls, image_id):
      return cls.objects.get(pk=image_id)

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(image_category__category_name__icontains=search_term)
        return news

    @classmethod
    def search_category(cls, categorys_name):
        return cls.objects.filter(image_category__category_name=categorys_name)

    @classmethod
    def filter_by_location(cls, location):
        return cls.objects.filter(image_location=location)

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image_url=value)
