# # ! view'da viewset kullandığımız için burda router kullanmamız gerekiyor
from rest_framework import routers
from .views import CategoryView, BrandView, ProductView, FirmView, TransactionView

router = routers.DefaultRouter()
# ! parantex içinde ilk yazılacak yer ile ikinci yere yalıcak yeri çalıştırıyoruz
router.register('categories', CategoryView)
router.register('brands', BrandView)
router.register('product', ProductView)
router.register('firm', FirmView)
router.register('transaction', TransactionView)


urlpatterns = [
    
]

urlpatterns += router.urls