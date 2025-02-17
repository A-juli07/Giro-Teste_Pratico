from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length= 100)
    type = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name

class Investor(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, related_name='exchange_rates', on_delete=models.CASCADE)
    date = models.DateField()
    daily_variation = models.FloatField()
    daily_rate = models.FloatField()

    def __str__(self):
        return f"{self.currency.name} ({self.date})"
    
class InvestmentHistory(models.Model):
    investor = models.ForeignKey(Investor, related_name='investments', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, related_name='investments', on_delete=models.CASCADE)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
    months= models.IntegerField()
    interest_rate = models.FloatField()
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Investimentos de {self.investor.name} em ({self.currency.name})"
