from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import os

TOKEN = os.getenv("BOT_TOKEN")  # Railway ke env variable se token lega

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! DailyEarnBot abhi live hai ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
