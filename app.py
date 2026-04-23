from flask import Flask, render_template, request
from market_data import get_stock_data
from ai_analyst import analyze_stock
import markdown
import json
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/analyze', methods=["POST"])
def analyze():
    ticker = request.form.get("ticker").upper()
    history, recent_news, x_data, y_data = get_stock_data(ticker)
    news_titles = [article["content"]["title"] for article in recent_news[:3]]
    raw_ai_response = analyze_stock(ticker, history['Close'].to_string(), "\n".join(news_titles))
    formatted_report = markdown.markdown(raw_ai_response)

    return render_template("analysis.html", report=formatted_report, ticker=ticker, x_data=json.dumps(x_data), y_data=json.dumps(y_data))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)