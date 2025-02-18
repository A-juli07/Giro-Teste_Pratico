from django.test import TestCase
from .models import Investor, Currency, InvestmentHistory
from rest_framework.test import APITestCase
from .serializers import CurrencySerializer

class CurrencyModelTest(TestCase):
    def test_create_currency(self):
        currency = Currency.objects.create(name="Real", type="R$")
        self.assertEqual(currency.name, "Real")
        self.assertEqual(currency.type, "R$")

class InvestmentHistoryModelTest(TestCase):
    def test_create_investment(self):
        investor = Investor.objects.create(name="João", email="joao@email.com")
        currency = Currency.objects.create(name="Euro", type="€")
        investment = InvestmentHistory.objects.create(
            investor=investor, currency=currency, initial_amount=1000.00, months=12, interest_rate=0.05, final_amount=1050.00
        )

        self.assertEqual(investment.investor.name, "João")
        self.assertEqual(investment.currency.name, "Euro")
        self.assertEqual(float(investment.final_amount), 1050.00)

