# # ! view'da viewset kullandığımız için burda router kullanmamız gerekiyor
from rest_framework import routers
from .views import CategoryView, BrandView, ProductView, FirmView, StockView

router = routers.DefaultRouter()
# ! parantex içinde ilk yazılacak yer ile ikinci yere yalıcak yeri çalıştırıyoruz
# router.register('categories', CategoryView)
# router.register('brands', BrandView)
# router.register('product', ProductView)
# router.register('firm', FirmView)
router.register('stock', StockView)


urlpatterns = [
    
]

urlpatterns += router.urls