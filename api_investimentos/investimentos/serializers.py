from rest_framework import serializers
from .models import Currency, Investor, ExchangeRate, InvestmentHistory

class CurrencySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Currency
        fields = '__all__'

class InvestorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Investor
        fields = '__all__'

class ExchangeRateSerializer(serializers.ModelSerializer):
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all()) 
    currency_type = serializers.CharField(source='currency.type', read_only=True)

    class Meta: 
        model = ExchangeRate
        fields = ['date', 'daily_variation', 'daily_rate','currency', 'currency_type']


class InvestmentHistorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = InvestmentHistory
        fields = '__all__'