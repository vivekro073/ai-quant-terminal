import yfinance as yf


def get_stock_data(ticker_symbol):
    print(f"Establishing connection to market data for: {ticker_symbol}...")
    stock = yf.Ticker(ticker_symbol)

    hist = stock.history(period="7d")
    x_data = hist.index.strftime('%Y-%m-%d').tolist()
    y_data = hist['Close'].round(2).tolist()

    news = stock.news

    return hist, news, x_data, y_data


if __name__ == "__main__":
    history, recent_news, x_data, y_data = get_stock_data("AAPL")

    print("\n--- 5-DAY PRICE ACTION ---")
    print(history['Close'])

    print("\n--- LIVE NEWS HEADLINES ---")
    for article in recent_news[:3]:
        print(article["content"]["title"])