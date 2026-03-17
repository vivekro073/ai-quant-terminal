import yfinance as yf
import pandas as pd

def get_stock_data(ticker_symbol):
    print(f"Establishing connection to market data for: {ticker_symbol}...")
    stock = yf.Ticker(ticker_symbol)

    hist = stock.history(period="5d")

    news = stock.news

    return hist, news


if __name__ == "__main__":
    history, recent_news = get_stock_data("AAPL")

    print("\n--- 5-DAY PRICE ACTION ---")
    print(history['Close'])

    print("\n--- LIVE NEWS HEADLINES ---")
    for article in recent_news[:3]:
        print(article["content"]["title"])