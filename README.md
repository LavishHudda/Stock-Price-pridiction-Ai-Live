# Indian Stock Market Prediction Platform (ANTIGRAVITY.AI)

A production-ready, feature-rich web application built with Python Flask and Machine Learning libraries to analyze and predict trends in the Indian Stock Market (NSE/BSE).

---

## Technical Stack

*   **Backend:** Python 3.10+ Flask
*   **Database:** SQLite (default for local development, switchable to PostgreSQL in `.env`)
*   **ML Engine:** Scikit-learn, XGBoost, TensorFlow, Pandas, NumPy
*   **Aesthetic styling:** Vanilla CSS with custom Glassmorphic variables, Bootstrap 5, Bootstrap Icons
*   **Charts:** Interactive Plotly.js charts (Candlestick + Technical Overlays)
*   **APIs:** yfinance (Yahoo Finance) for free, live, and historical Indian stocks data (e.g. `RELIANCE.NS`, `TCS.NS`, `^NSEI` Nifty 50 index)
*   **AI Chatbot Assistant:** Gemini Flash 1.5 API (with a smart rules-based fallback if no API key is specified)

---

## Core Features

1.  **Live Indian Stock Data:** Live index tickers (Nifty 50, Sensex, Bank Nifty) scrolling at the top, autocomplete search capability for NSE/BSE symbols, and full detailed statistics.
2.  **Interactive Analysis Dashboard:** Candlestick charts with switches to overlay Bollinger Bands, SMA 20, SMA 50, and SMA 200. Toggle panels for RSI, MACD, and Volume histograms.
3.  **AI Predictions Engine:** Forecasts next-day, weekly, and monthly close prices using Linear Regression, Random Forest, XGBoost, and LSTM neural networks. Provides a consolidated weighted price target, directional signal, and confidence score.
4.  **Portfolio Simulator:** Mock trading center where users receive ₹1,000,000 INR of virtual cash on sign up to purchase or sell shares with real live market prices. Tracks holdings and logs transactions.
5.  **Watchlist Manager:** Star/unstar stocks directly from search autocompletes, home market table, or dashboard.
6.  **AI Assistant Chatbot:** Integrates chatbot dialog queries. Mentions of popular tickers fetch live stock numbers on the fly.
7.  **Admin Panel:** System logs, user lists, and model training scheduler running training threads in background.

---

## Project Structure

```
├── app.py                  # Main entry point and Flask application factory
├── config.py               # Settings and directory bootstrapping
├── requirements.txt        # Backend dependencies list
├── .env                    # System secrets (ignored in git)
├── .env.example            # Environment variables template
├── test_ml_and_data.py     # Verification script to test backend models
├── Dockerfile              # Container building instructions
├── docker-compose.yml      # Multi-container orchestration (web + database)
├── nginx.conf              # Reverse proxy server config with rate limiting
├── models/                 # SQLAlchemy DB schemas
│   ├── __init__.py
│   ├── user.py
│   ├── watchlist.py
│   ├── portfolio.py
│   └── prediction_logs.py
├── routes/                 # Flask Blueprints
│   ├── __init__.py
│   ├── auth.py
│   ├── main.py
│   ├── api.py
│   └── admin.py
├── services/               # Core business services
│   ├── __init__.py
│   ├── market_data.py
│   ├── indicators.py
│   ├── prediction_engine.py
│   └── chatbot.py
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Premium custom stylesheets (dark mode)
│   └── js/
│       ├── main.js         # General autocompletion and watchlist click actions
│       ├── dashboard.js    # Interactive chart and trading order handlers
│       └── chat.js         # AI dialog rendering with markdown parser
└── templates/              # Jinja2 HTML layout views
    ├── base.html           # Shared sidebar header
    ├── index.html          # Markets home dashboard
    ├── login.html          # User login
    ├── register.html       # User register
    ├── dashboard.html      # Interactive Plotly stock dashboard
    ├── watchlist.html      # Starred listings
    ├── portfolio.html      # Simulator balance & orders ledger
    ├── chatbot.html        # Assistant dashboard
    └── admin.html          # Model logs and retraining trigger
```

---

## Getting Started

### 1. Prerequisite Installations
Ensure you have Python 3.10+ installed on your computer.

### 2. Install Packages
In your terminal, navigate to the project directory and run:
```bash
pip install -r requirements.txt
```

### 3. Setup Environment variables
A `.env` file is already preconfigured in the workspace root for local SQLite operations. 
If you want to use the AI chatbot with Gemini:
Open the `.env` file and set `GEMINI_API_KEY=your_key`. Otherwise, the local rule-based technical analyst fallback answers queries.

### 4. Run Verification Suite
Run the test suite to ensure yfinance, indicator computation, and ML training pipelines are executing cleanly:
```bash
python test_ml_and_data.py
```

### 5. Start Application
```bash
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your web browser.

*   **Default Admin Account:**
    *   **Username:** `admin`
    *   **Password:** `admin123`

---

## Production Deployment

### Docker setup
Start containerization with Docker Compose:
```bash
docker-compose up --build -d
```
This builds the Flask app with Gunicorn, binds port 5000, and mounts SQLite volumes.

### Nginx setup
Map `nginx.conf` to Nginx container volumes or proxy traffic to port 5000 on your host. The included Nginx setup adds rate limiting (`10 requests/sec`) for `/api/` endpoints to prevent scraping abuse and adds critical HTTP security headers.
