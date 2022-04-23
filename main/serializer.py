from dataclasses import fields
from rest_framework import serializers
from .models import *

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

class ContactinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactinfo
        fields = '__all__'

class HeaderSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderSlider
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DiscountItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountItems
        fields = '__all__'

class BrandSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandSlider
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 2

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class NewsletterBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterBlog
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

class ContactBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBlog
        fields = '__all__'

class GetintouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Getintouch
        fields = '__all__'




































