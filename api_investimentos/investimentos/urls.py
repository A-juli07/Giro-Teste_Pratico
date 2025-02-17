from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, InvestorViewSet, ExchangeRateViewSet, InvestmentHistoryViewSet

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'investors', InvestorViewSet)
router.register(r'exchange-rates', ExchangeRateViewSet)
router.register(r'investments', InvestmentHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
