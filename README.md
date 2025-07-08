# TashanWin Predictor Bot

A Telegram bot that fetches live WinGo 30s results and predicts the next outcome using LCG + Markov + RickRules.

### 🔧 Setup Instructions (Render.com)

1. Visit https://render.com and create an account
2. Click **"New Web Service"** > **"Deploy from GitHub"**
3. Upload these files to a GitHub repo or drag into the "Manual Deploy"
4. Set runtime: **Python 3.10+**
5. Add build command:
    ```
    pip install -r requirements.txt
    ```
6. Add start command:
    ```
    python main.py
    ```
7. Add **Environment Variable**:
    - `BOT_TOKEN` = your Telegram bot token

You're done! Your bot is now live.

Use /start, /predict, /live, /trap inside Telegram.

Enjoy 🧠🎯