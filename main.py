import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from predictor import get_prediction
from api import fetch_latest_result
from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to TashanWin Predictor Bot!\nUse /predict to get the next outcome.\nUse /live to see the current result.\nUse /trap to detect traps.")

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = fetch_latest_result()
    await update.message.reply_text(f"📊 Latest Result:\nNumber: {result['number']}\nColor: {result['color']}\nSize: {result['size']}\nPeriod: {result['period']}")

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prediction = get_prediction()
    await update.message.reply_text(prediction)

async def trap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trap_message = "⚠️ Trap Alert: 5 or 0 has appeared too frequently. Avoid if they repeat."
    await update.message.reply_text(trap_message)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("live", live))
app.add_handler(CommandHandler("predict", predict))
app.add_handler(CommandHandler("trap", trap))

app.run_polling()