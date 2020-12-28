import finnhub
from api_keys.stock import api_key
import math


class Stock:
    def __init__(self):
        self.name = None
        self.current_price = 0
        self.percentage = 0
        self.high_price = 0
        self.low_price = 0
        self.open_price = 0
        self.image = None


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def basic_stock_return(name_of_company):
    stonk = Stock()
    client = finnhub.Client(api_key=api_key)
    quote_data = client.quote(name_of_company)
    company_profile = client.company_profile(symbol=name_of_company)
    stonk.name = company_profile["name"]
    stonk.current_price = quote_data["c"]
    stonk.open_price = quote_data["o"]
    stonk.high_price = quote_data["h"]
    stonk.low_price = quote_data["l"]
    stonk.image = company_profile["logo"]
    stonk.high_price = quote_data["h"]
    stonk.percentage = truncate(
        (100 * (stonk.current_price - stonk.open_price) / stonk.open_price), 2
    )
    return stonk
