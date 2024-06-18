from . import views
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CouponViewSet, TransactionViewSet, SwapViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'swaps', SwapViewSet)

urlpatterns = [
    path("",views.home,name="home"),
     path('', include(router.urls)),
    
]
