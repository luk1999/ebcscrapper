from rest_framework import serializers

from scrapper import models


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = (
            'symbol',
            'name',
        )


class CurrencyRateSerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField()
    main_currency = serializers.SerializerMethodField()

    class Meta:
        model = models.CurrencyRate
        fields = (
            'currency',
            'main_currency',
            'rate',
            'updated_at',
        )

    def get_currency(self, rate):
        """
        :type rate: scrapper.models.CurrencyRate
        :rtype: string
        """
        return rate.currency.symbol

    def get_main_currency(self, rate):
        """
        :type rate: scrapper.models.CurrencyRate
        :rtype: string
        """
        return rate.main_currency.symbol
