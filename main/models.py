import re
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'client'),
        (3, 'worker')
    ), default=2)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Logo(models.Model):
    img = models.ImageField(upload_to='media/')

class Contactinfo(models.Model):
    phone = models.CharField(max_length=25)
    email = models.EmailField()

class HeaderSlider(models.Model):
    title = models.CharField(max_length=255)
    para = models.CharField(max_length=255)
    img = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.title

class Service(models.Model):
    img = models.ImageField(upload_to='service/')
    title = models.CharField(max_length=255)
    para = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class DiscountItems(models.Model):
    img = models.ImageField(upload_to='media/')
    percentage = models.IntegerField()
    title = models.CharField(max_length=255)
    para = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class BrandSlider(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SocialMedia(models.Model):
    link = models.CharField(max_length=5000)
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='products/')
    discount = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price =  models.DecimalField(max_digits=7, decimal_places=2)
    popularity = models.FloatField()

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    orderitem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Sale(models.Model):
    img = models.ImageField(upload_to='sale/')

class Collection(models.Model):
    title = models.CharField(max_length=255)

class NewsletterBlog(models.Model):
    bgimg = models.ImageField(upload_to='newsletterblog/')
    titleleft = models.CharField(max_length=255)
    titleright = models.CharField(max_length=255)
    link1 = models.CharField(max_length=5000)
    link2 = models.CharField(max_length=5000)

class Newsletter(models.Model):
    email = models.EmailField()

# Contact Blog

class ContactBlog(models.Model):
    bgimg = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    para = models.CharField(max_length=255)
    map = models.CharField(max_length=5000)
    phone1 = models.CharField(max_length=25)
    phone2 = models.CharField(max_length=25)
    email = models.EmailField()
    website = models.CharField(max_length=5000)
    address = models.CharField(max_length=255)

class Getintouch(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=3000)
