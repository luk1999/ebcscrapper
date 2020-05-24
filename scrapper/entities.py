from collections import namedtuple


# @TODO: Replace by dataclass later
CurrencyRateEntry = namedtuple('CurrencyRateEntry', (
    'currency',
    'currency_name',
    'main_currency',
    'main_currency_name',
    'rate',
    'updated_at',
))
