from django.test import TestCase
from .models import Location, Category, Image
from django.utils import timezone
# Create your tests here.
class ImageTestClass(TestCase):

    # set up 
    def setUp(self):
        self.location = Location(location_name='nairobi')
        self.location.save()
        # categories
        self.category = Category(category_name='nairobi')
        self.category.save()

        # image
        self.image = Image(image_name='peter', image_description='kkkkkk', image_location=self.location, image_category=self.category, pub_date=timezone.now(), image_url='~/Download/grenade.jpg')

    # clean up after every test
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    # est save in method
    def test_save(self):
        self.image
        self.image.image_save()
        self.assertTrue(len(Image.objects.all())>0)

    # test delete
    def test_delete(self):
        self.image
        self.image.image_save()
        self.image1 = Image(image_name='peter', image_description='kkkkkk', image_location=self.location,
                                   image_category=self.category, pub_date=timezone.now(), image_url='~/Download/grenade.jpg')
        
        self.image1.image_save()
        self.image1.image_delete()
        self.assertTrue(len(Image.objects.all()) == 1)

    # test getting image by id
    def test_get_image_by_Id(self):
        self.image.image_save()
        test_image = Image(image_name='peter', image_description='kkkkkk', image_location=self.location,
                          image_category=self.category, pub_date=timezone.now(), image_url='~/Download/grenade.jpg')
        test_image.image_save()
        found_image = Image.objects.get(pk=test_image.id)
        filters = Image.get_image_by_Id(test_image.id)
        self.assertEqual(found_image, filters)

    def test_search_by_category(self):
        self.image.image_save()
        test_image = Image(image_name='peter', image_description='kkkkkk', image_location=self.location,
                           image_category=self.category, pub_date=timezone.now(), image_url='~/Download/grenade.jpg')
        test_image.image_save()
        found_image = Image.search_category(test_image.image_category)
        # filters = Image.search_category(test_image.image_category)
        self.assertTrue(len(found_image)==2)

    def test_filter_by_location(self):
        self.image.image_save()
        test_image = Image(image_name='peter', image_description='kkkkkk', image_location=self.location,
                           image_category=self.category, pub_date=timezone.now(), image_url='~/Download/grenade.jpg')
        test_image.image_save()
        found_images = Image.filter_by_location(test_image.image_location)
        self.assertTrue(len(found_images)>1) 

    def test_update_image(self):
        self.image.image_save()
        found_update = Image.objects.filter(id=self.image.id).update(image_url='value')
        new_image = Image.objects.filter(image_url='value')
        self.assertTrue(len(new_image)> 0)
