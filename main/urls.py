from django.urls import path, include
from .router import *

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductViews),
    path('sliders/', SliderGET),
    path('bycategory/', Bycategory),
    path('byname/', Byname),
    path('byprice/', ByPrice),
    path('bydiscount/', Bydiscount),
    path('towishlist/', Addtowishlist),
    path('delwishlist/', Deletefromwishlist),
    path('tocard/', Addtocard),
    path('delcard/', DeleteFromCard),
    path('patchcard/', Patchcard),
    path('orderitem/', ByOrderitem),
    path('history/', History),
]