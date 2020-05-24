from . import (
    readers,
    writers,
)

CURRENCIES_TO_IMPORT = (
    'usd',
    'jpy',
    'pln',
    'gbp',
)


class ScrapperService:
    @staticmethod
    def save_latest_rates():
        reader = readers.CurrencyRateReader()
        writer = writers.CurrencyRateWriter()
        for currency in CURRENCIES_TO_IMPORT:
            entry = reader.get_latest(currency)
            writer.save(entry)
