from django.db import models


class Currency(models.Model):
    symbol = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.symbol


class CurrencyRate(models.Model):
    main_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='main_currency'
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name='currency'
    )
    rate = models.DecimalField(max_digits=10, decimal_places=6)
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.currency}/{self.main_currency} rate: {self.rate}'
