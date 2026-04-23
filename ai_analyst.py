from google import genai
from dotenv import load_dotenv
from market_data import get_stock_data
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_stock(ticker_symbol, price_history, news_headlines):
    prompt = f"""You are an expert quantitative financial analyst at a top-tier hedge fund. 
        I am providing you with the latest 5-day price history and the most recent news headlines for the stock ticker: {ticker_symbol}.

        DATA:
        --- 5-Day Price History ---
        {price_history}

        --- Recent News Headlines ---
        {news_headlines}

        YOUR TASK:
        Analyze the short-term price trend and the sentiment of the news headlines. 

        OUTPUT FORMAT:
        You must format your response strictly in HTML. Do not use markdown. Do not use ```html codeblocks. Return ONLY the raw HTML using this exact structure:

        <strong>BUY</strong>
        <ul>
            <li>Your first concise bullet point based on data.</li>
            <li>Your second concise bullet point based on data.</li>
            <li>Your third concise bullet point based on data.</li>
        </ul>

        If your signal is HOLD or SELL, replace the word BUY inside the <strong> tags. Do not include any conversational filler."""
    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
    return response.text
