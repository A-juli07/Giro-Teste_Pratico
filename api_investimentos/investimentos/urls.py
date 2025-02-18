from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, InvestorViewSet, ExchangeRateViewSet, InvestmentHistoryViewSet

#Rotas da api

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'investors', InvestorViewSet)
router.register(r'exchange-rates', ExchangeRateViewSet)
router.register(r'investments', InvestmentHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('exchange-rates/old/', ExchangeRateViewSet.as_view({'delete': 'old'}), name='exchange-rate-old'),
    path('exchange-rates/<int:id>/', ExchangeRateViewSet.as_view({'put': 'update'}), name='exchange-rate-detail'),
    path('investors/<int:id>/', InvestorViewSet.as_view({'delete': 'destroy'}), name='investor-detail'),

]
