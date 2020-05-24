import datetime
import decimal
import http
import re
import time

import feedparser

from . import (
    entities,
    exceptions,
)


class CurrencyRateReader:
    url_pattern = 'https://www.ecb.europa.eu/rss/fxref-{currency}.html'
    # This could not be extracted from feed
    main_currency_name = 'EURO'

    def get_latest(self, currency):
        """
        :type currency: str
        :rtype:
        """
        entries = self._get_all_entries(currency)

        try:
            entry = entries[0]
        except KeyError:
            raise exceptions.CurrencyEntryDoesNotExistError()

        entry = self._parse_entry(entry)

        return entry

    def _get_all_entries(self, currency):
        """
        :type currency: str
        :rtype: list
        """
        url = self.url_pattern.format(currency=currency)
        document = feedparser.parse(url)

        http_status = document['status']

        if http_status == http.HTTPStatus.NOT_FOUND:
            raise exceptions.CurrencyDoesNotExistError(f'Currency {currency} does not exist')

        if http_status != http.HTTPStatus.OK:
            raise exceptions.CurrencyDoesNotExistError(f'Could not load page {url}')

        return document.entries

    def _parse_entry(self, entry):
        """
        :type entry: dict
        :rtype: scrapper.entities.CurrencyRateEntry
        """
        try:
            summary_detail = entry['summary_detail']
            value = summary_detail['value']
            updated_parsed = entry['updated_parsed']
        except KeyError as e:
            raise exceptions.CurrencyParseError(f'Could not parse entry. {e}')

        try:
            currency, currency_name, main_currency, rate = self._parse_value(value)
            updated_at = self._parse_updated_parsed(updated_parsed)
        except ValueError as e:
            raise exceptions.CurrencyParseError(f'Could not convert value when parsing. {e}')

        return entities.CurrencyRateEntry(
            currency=currency,
            currency_name=currency_name,
            main_currency=main_currency,
            main_currency_name=self.main_currency_name,
            rate=rate,
            updated_at=updated_at,
        )

    def _parse_value(self, value):
        """
        :rtype: tuple
        """
        # Parses string like 1 EUR buys 1.0904 US dollar (USD) - The reference...
        # @TODO: This should be done using regexp
        value, unused = value.split(' - The reference exchange rates')
        _unused, main_currency, _unused, rate, *currency_name = value.split(' ')

        rate = decimal.Decimal(rate)
        currency = re.sub('[^A-Z]+', '', currency_name.pop())
        currency_name = ' '.join(currency_name)
        return currency, currency_name, main_currency, rate

    def _parse_updated_parsed(self, updated_parsed):
        """
        :type updated_parsed: time.struct_time
        :rtype: datetime.datetime
        """
        updated_ts = time.mktime(updated_parsed)
        return datetime.datetime.fromtimestamp(updated_ts)
