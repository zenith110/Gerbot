import finnhub
import requests_cache
class Stock():
    def __init__(self):
        self.name = None
        self.current_price = 0
        self.percentage = 0
        self.high_price = 0
        self.low_price = 0
        self.open_price = 0
        self.image = None
def basic_stock_return(name_of_company):
    stonk = Stock()
    client = finnhub.Client(api_key="bssmob748v6thfcovci0")
    quote_data  = client.quote(name_of_company)
    company_profile = client.company_profile(symbol=name_of_company)
    stonk.name = company_profile["name"]
    stonk.current_price = quote_data["c"]
    stonk.open_price = quote_data["o"]
    stonk.high_price = quote_data["h"]
    stonk.low_price = quote_data["l"]
    stonk.image = company_profile["logo"]
    stonk.high_price = quote_data["h"]
    return stonk
