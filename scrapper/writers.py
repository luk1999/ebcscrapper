from . import models


class CurrencyRateWriter:
    def save(self, entry):
        """
        :type entry: scrapper.entities.CurrencyRateEntry
        :rtype: scrapper.models.CurrencyRate
        """
        currency_obj = self._get_or_create_currency(
            entry.currency,
            entry.currency_name
        )
        main_currency_obj = self._get_or_create_currency(
            entry.main_currency,
            entry.main_currency_name
        )

        rate_obj, _created = models.CurrencyRate.objects.get_or_create(
            main_currency=main_currency_obj,
            currency=currency_obj,
            updated_at=entry.updated_at,
            defaults={'rate': entry.rate}
        )

        return rate_obj

    def _get_or_create_currency(self, currency, currency_name):
        """
        :str currency:
        :str currency_name:
        :rtype: scrapper.models.Currency
        """
        # @TODO: Cache currency_obj and currency_main_obj for better performance
        currency_obj, _created = models.Currency.objects.get_or_create(
            symbol=currency,
            defaults={'name': currency_name}
        )
        return currency_obj
