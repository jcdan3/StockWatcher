from settings import GetSettings
from StockGetter import GetStockPrice

if __name__ == "__main__":
    settings = GetSettings("settings.json")
    stocksprice = GetStockPrice(settings.get("Stocks"))