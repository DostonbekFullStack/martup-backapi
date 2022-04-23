from .serializer import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# HOME

# class LogoViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = Logo.objects.all()
#     serializer_class = LogoSerializer

#     def list(request, self):
#         logo = Logo.objects.last()
#         ser = LogoSerializer(logo, many=False)
#         return Response(ser.data)

# class ContactinfoViews(viewsets.ModelViewSet):
#     queryset = Contactinfo.objects.all()
#     serializer_class = ContactinfoSerializer

#     def list(self, request):
#         contacts = Contactinfo.objects.last()
#         ser = ContactinfoSerializer(contacts, many=False)
#         return Response(ser.data)

#     def create(self, request):
#         try:
#             phone = request.data['phone']
#             email = request.data['email']
#             Contactinfo.objects.create(phone=phone, email=email)
#             data = {
#                 'status': 200,
#             }
#             return Response(data)
#         except Exception as err:
#             data = {
#                 'error': f'{err}'
#             }
#             return Response(data)

# class HeaderSliderViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = HeaderSlider.objects.all()
#     serializer_class = HeaderSliderSerializer

#     def list(self,request):
#         headerslider = HeaderSlider.objects.all().order_by('-id')[0:3]
#         ser = HeaderSliderSerializer(headerslider, many=True)
#         return Response(ser.data)

# class ServiceViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

#     def list(self, request):
#         service = Service.objects.all().order_by('-id')[0:3]
#         ser = ServiceSerializer(service, many=True)
#         return Response(ser.data)
    
#     def create(self,request):
#         try:
#             img = request.FILES['img']
#             title = request.data['title']
#             para = request.data['para']
#             Service.objects.create(img=img, title=title, para=para)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as err:
#             data = {
#                 'error': f"{err}"
#             }
#             return Response(data)

# class DiscountItemsViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = DiscountItems.objects.all()
#     serializer_class = DiscountItemsSerializer

#     def list(self, request):
#         discountitems = DiscountItems.objects.all().order_by('-id')[0:3]
#         ser = DiscountItemsSerializer(discountitems, many=True)
#         return Response(ser.data)
    

# class BrandSliderViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = BrandSlider.objects.all()
#     serializer_class = BrandSliderSerializer

#     def list(self, request):
#         brandslider = BrandSlider.objects.all()
#         ser = BrandSliderSerializer(brandslider, many=True)
#         return Response(ser.data)
        
# class SocialMediaViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = SocialMedia.objects.all()
#     serializer_class = SocialMediaSerializer

#     def list(self, request):
#         socialmedia = SocialMedia.objects.all().order_by('-id')[0:4]
#         ser = SocialMediaSerializer(socialmedia, many=True)
#         return Response(ser.data)
    

# class ProductViews(viewsets.ModelViewSet):
#     http_method_names=['get', 'post']
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def list(self, request):
#         product = Product.objects.all()
#         ser = ProductSerializer(product, many=True)
#         return Response(ser.data)
    
#     def create(self,request):
#         try:
#             img = request.FILES['img']
#             discount = request.data['discount']
#             category = request.data['category']
#             name = request.data['name']
#             price = request.data['price']
#             popularity = request.data['popularity']
#             Product.objects.create(img=img, discount=discount, name=name, category_id=category, price=price, popularity=popularity)
#             data = {
#                 'status': 200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'status': f'{er}'
#             }
#             return Response(data)

# @api_view(['GET'])
# def wishlistview(request):
#         wishlist = Wishlist.objects.all()
#         ser = WishlistSerializer(wishlist, many=True)
#         return Response(ser.data)

# class WishlistViews(viewsets.ModelViewSet):
#     queryset = Wishlist.objects.all()
#     serializer_class = WishlistSerializer
    
#     def create(self, request):
#         try:
#             product = request.data['product']
#             quantity = request.data['quantity']
#             Wishlist.objects.create(product_id=product, quantity=quantity)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f"{er}"
#             }
#             return Response(data)
    
#     def destroy(self, request):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CardViews(viewsets.ModelViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer

#     def list(request, self):
#         card = Card.objects.all()
#         ser = CardSerializer(card, many=True)
#         return Response(ser.data)
    
#     def create(self, request):
#         try:
#             product = request.data['product']
#             quantity = request.data['quantity']
#             Card.objects.create(product_id=product, quantity=quantity)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f"{er}"
#             }
#             return Response(data)

# class SaleViews(viewsets.ModelViewSet):
#     http_method_names=['get']
#     queryset = Sale.objects.all()
#     serializer_class = SaleSerializer

#     def list(self, request):
#         sale = Sale.objects.last()
#         ser = SaleSerializer(sale, many=False)
#         return Response(ser.data)
    
# class CollectionViews(viewsets.ModelViewSet):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer

#     def list(self, request):
#         collection = Collection.objects.last()
#         ser = CollectionSerializer(collection, many=False)
#         return Response(ser.data)

#     def create(self, request):
#         try:
#             title = request.data['title']
#             Collection.objects.create(title=title)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f'{er}'
#             }
#             return Response(data)

# class NewsletterBlogViews(viewsets.ModelViewSet):
#     queryset = NewsletterBlog.objects.all()
#     serializer_class = NewsletterBlogSerializer

#     def list(self, request):
#         newsletterblog = NewsletterBlog.objects.last()
#         ser = NewsletterBlogSerializer(newsletterblog, many=True)
#         return Response(ser.data)
    
#     def create(self, request):
#         try:
#             bgimg = request.data['bgimg']
#             titleleft = request.data['titleleft']
#             titleright = request.data['titleright']
#             link1 = request.data['link1']
#             link2 = request.data['link2']
#             NewsletterBlog.objects.create(bgimg=bgimg, titleleft=titleleft, titleright=titleright, link1=link1,link2=link2)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f'{er}'
#             }
#             return Response(data)

# class NewsletterViews(viewsets.ModelViewSet):
#     queryset = Newsletter.objects.all()
#     serializer_class = NewsletterSerializer

#     def list(self, request):
#         newsletter = Newsletter.objects.all()
#         ser = NewsletterSerializer(newsletter, many=True)
#         return Response(ser.data)
    
#     def create(self, request):
#         try:
#             email = request.data['email']
#             Newsletter.objects.create(email=email)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f'{er}'
#             }
#             return Response(data)

# #


# # CONTACT 

# class ContactBlogViews(viewsets.ModelViewSet):
#     queryset = ContactBlog.objects.all()
#     serializer_class = ContactBlogSerializer

#     def list(self, request):
#         contactblog = ContactBlog.objects.last()
#         ser = ContactBlogSerializer(contactblog, many=False)
#         return Response(ser.data)
    
#     def create(self, request):
#         try:
#             bgimg = request.FILES['bgimg']
#             title = request.data['title']
#             para = request.data['para']
#             map = request.data['map']
#             phone1 = request.data['phone1']
#             phone2 = request.data['phone2']
#             email = request.data['email']
#             website = request.data['website']
#             address = request.data['address']
#             ContactBlog.objects.create(bgimg=bgimg, title=title, para=para, map=map, phone1=phone1, phone2=phone2, email=email, website=website, address=address)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f'{er}'
#             }
#             return Response(data)

# class GetintouchViews(viewsets.ModelViewSet):
#     queryset = Getintouch.objects.all()
#     serializer_class = GetintouchSerializer

#     def list(self, request):
#         getintouch = Getintouch.objects.all()
#         ser = GetintouchSerializer(getintouch, many=True)
#         return Response(ser.data)
    
#     def create(self, request):
#         try:
#             email = request.data['email']
#             name = request.data['name']
#             subject = request.data['subject']
#             message = request.data['message']
#             Getintouch.objects.create(name=name, email=email, subject=subject, message=message)
#             data = {
#                 'status':200
#             }
#             return Response(data)
#         except Exception as er:
#             data = {
#                 'error': f'{er}'
#             }
#             return Response(data)
# # 


# API VIEW 

@api_view(['GET'])
def ProductViews(request):
    product = Product.objects.all()
    ser = ProductSerializer(product, many=True)
    return Response(ser.data)

@api_view(['GET'])
def SliderGET(request):
    slider = HeaderSlider.objects.all().order_by('-id')[0:3]
    ser = HeaderSliderSerializer(slider, many=True)
    return Response(ser.data)

@api_view(["GET"])
def Bycategory(request):
    category = request.GET.get('category')
    product = Product.objects.filter(category_id=category)
    pro = ProductSerializer(product, many=True)
    return Response(pro.data)

@api_view(['GET'])
def Byname(request):
    name = request.GET.get('name')
    product = Product.objects.get(name__icontains=name)
    pro = ProductSerializer(product)
    return Response(pro.data)

@api_view(['GET'])
def ByPrice(request):
    price = request.GET.get('price')
    pri = Product.objects.filter(price=price)
    pr = ProductSerializer(pri, many=True)
    return Response(pr.data)

@api_view(['GET'])
def Bydiscount(reqeuest):
    discoun = Product.objects.all().order_by('-discount')
    ser = ProductSerializer(discoun, many=True)
    return Response(ser.data)

@api_view(['POST'])
def Addtowishlist(request):
    id = request.GET.get('id')
    product = Product.objects.get(id=id)
    Wishlist.objects.create(product=product)
    return Response('success')

@api_view(['POST'])
def Deletefromwishlist(request):
    id = request.GET.get('id')
    wishlist = Wishlist.objects.get(id=id)
    wishlist.delete()
    return Response(f'deleted-{id}')

@api_view(['POST'])
def Addtocard(request):
    id = request.GET.get('id')
    quan = request.GET.get('quantity')
    product = Product.objects.get(id=id)
    Card.objects.create(product=product, quantity=quan)
    return Response('success')

@api_view(['POST'])
def DeleteFromCard(request):
    id = request.GET.get('id')
    card = Card.objects.get(id=id)
    card.delete()
    return Response(f'deleted-{id}')

api_view(['PATCH'])
def Patchcard(request):
    id = request.GET.get('id')
    quan = request.GET.get('quantity')
    card = Card.objects.get(id=id, quantity=quan)
    card.save()
    return Response('changed')

@api_view(["GET"])
def ByOrderitem(request):
    orderi = OrderItem.objects.all()
    total_price = 0
    dat = []
    total = 0
    for i in orderi:
        total_price = i.quantity * i.product.price
        data = {
            'name': i.product.name,
            "total_price":total_price
        }
        total += total_price
        dat.append(data)
    dat.append(f"total: {total}")
    return Response(dat)

@api_view(['GET'])
def History(request):
    order = Order.objects.all()
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)