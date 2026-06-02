# AI Quant Terminal & Market Sentiment Digest 📈

An automated financial analysis engine that extracts real-time stock market data (such as top gainers and losers) and leverages Generative AI to generate instant, human-readable market sentiment digests.

## 📌 Business Value
Manual financial research requires navigating multiple platforms to aggregate price movements and news. This application automates the data engineering pipeline, pulling raw market metrics and passing them through an LLM to synthesize concise, actionable financial summaries. It demonstrates end-to-end backend development, from API data extraction to production-ready web deployment.

## ⚙️ Architecture & Data Flow
1. **Data Ingestion:** Utilizes `yfinance` to scrape and extract live market data, stock histories, and performance metrics.
2. **Data Processing:** Cleans, structures, and formats the raw financial data using `pandas` DataFrames.
3. **AI Analysis:** Transmits the structured data to Google's Gemini LLM to interpret market sentiment and generate a comprehensive markdown report.
4. **Backend Serving:** A `Flask` application routes the incoming requests, processes the AI's markdown output into readable HTML, and serves the frontend dashboard.
5. **Production Deployment:** Configured with `gunicorn` to ensure the application can handle concurrent requests in a production server environment.

## 🛠️ Tech Stack
* **Backend Framework:** Python, Flask
* **Production Server:** Gunicorn
* **Data Engineering:** Pandas, yfinance
* **Generative AI:** Google Gemini (`google-genai`)
* **Utilities:** python-dotenv (environment management), Markdown (text processing)

## 🚀 Local Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/vivekro073/ai-quant-terminal.git](https://github.com/vivekro073/ai-quant-terminal.git)
cd ai-quant-terminal