class URLReadError(Exception):
    ...


class CouldNotLoadUrlError(URLReadError):
    ...


class CurrencyDoesNotExistError(URLReadError):
    ...


class CurrencyEntryDoesNotExistError(URLReadError):
    ...


class CurrencyParseError(Exception):
    ...
