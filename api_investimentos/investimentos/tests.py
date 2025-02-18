from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Currency, Investor, ExchangeRate, InvestmentHistory
from datetime import datetime, timedelta

##Esse teste cria um objeto Currency e verifica se os valores foram salvos corretamente

class CurrencyModelTest(TestCase):
    def test_create_currency(self):
        currency = Currency.objects.create(name="Real", type="R$")

        print(f"Moeda criada: {currency.name} ({currency.type})")
        
        self.assertEqual(currency.name, "Real")
        self.assertEqual(currency.type, "R$")

##Esse teste cria um investimento e verifica se os dados estão corretos

class InvestmentHistoryModelTest(TestCase):
    def test_create_investment(self):
        investor = Investor.objects.create(name="João", email="joao@email.com")
        currency = Currency.objects.create(name="Euro", type="€")
        investment = InvestmentHistory.objects.create(
            investor=investor, currency=currency, initial_amount=1000.00, months=12, interest_rate=0.05, final_amount=1050.00
        )
        
        print(f"Investidor criado: {investor.name} ({investor.email})")
        print(f"Currency: {currency.name} ({currency.type})")
        print(f"Investimento: {investment.investor} ({investment.currency}) {investment.initial_amount} {investment.months} {investment.interest_rate} {investment.final_amount}")

        self.assertEqual(investment.investor.name, "João")
        self.assertEqual(investment.currency.name, "Euro")
        self.assertEqual(float(investment.final_amount), 1050.00)

#Testa o update dos dados da moeda e a exclusão de dados com mais de 30 dias 

class ExchangeRateAPITestCase(APITestCase):
    def test_update_exchange_rate(self):
        currency = Currency.objects.create(name="Dólar", type="USD")
        exchange_rate = ExchangeRate.objects.create(
            currency=currency, date=datetime.now(), daily_variation=0.1, daily_rate=5.20
        )
        url = reverse('exchange-rate-detail', args=[exchange_rate.id])

        data = {"currency": currency.id,"date": datetime.now().date().isoformat(), "daily_variation": 0.2, "daily_rate": 5.30}
        response = self.client.put(url, data, format='json')

        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        exchange_rate.refresh_from_db()
        self.assertEqual(float(exchange_rate.daily_rate), 5.30)


    def test_delete_old_exchange_rates(self):
        self.currency = Currency.objects.create(name="Dólar", type="Moeda Estrangeira")

        
        self.old_rates = [
            ExchangeRate.objects.create(
                currency=self.currency,
                date=datetime.now() - timedelta(days=31),
                daily_variation=0.1,
                daily_rate=5.20
            )
            for _ in range(3)
        ]

    
        self.recent_rates = [
            ExchangeRate.objects.create(
                currency=self.currency,
                date=datetime.now(),
                daily_variation=0.2,
                daily_rate=5.25
            )
        ]

        
        self.url_delete_old = reverse('exchange-rate-old')  

        response = self.client.delete(self.url_delete_old)
        print(response.data)
        
        if self.old_rates:
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)

#Verifica a exclusão de um investidor

class InvestorAPITestCase(APITestCase):
    def test_delete_investor_and_investments(self):
        self.currency = Currency.objects.create(name="Euro", type="EUR")
        self.investor = Investor.objects.create(name="Alice", email="alice@example.com")
        self.investment = InvestmentHistory.objects.create(
            investor=self.investor,
            currency=self.currency,
            initial_amount=1000.00,
            months=12,
            interest_rate=5.0,
            final_amount=1200.00
        )

        
        url = reverse('investor-detail', args=[self.investor.id])

        
        response = self.client.delete(url)
        print(response.data)

        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Investor.objects.filter(id=self.investor.id).exists())
        self.assertFalse(InvestmentHistory.objects.filter(id=self.investment.id).exists())

