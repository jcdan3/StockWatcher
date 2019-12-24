import yahoo_finance as yf

def GetStockPrice(stock_list):
    price_dict = {}
    for stock in stock_list:
        price_dict[stock] = yf.Share(stock).get_price()
    return price_dict