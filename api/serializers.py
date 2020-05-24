from rest_framework import serializers

from scrapper import models


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CurrencyRate
        fields = (
            'currency'
            'main_currency',
            'rate',
            'updated_at',
        )
