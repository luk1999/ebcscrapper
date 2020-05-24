from . import (
    constants,
    readers,
    writers,
)


class ScrapperService:
    @staticmethod
    def save_latest_rates():
        reader = readers.CurrencyRateReader()
        writer = writers.CurrencyRateWriter()
        for currency in constants.CURRENCIES:
            entry = reader.get_latest(currency)
            writer.save(entry)
