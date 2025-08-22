from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === Apna Bot Token yaha daalo ===
TOKEN = ""8208891679:AAE6j5aVkxE8SsAJyLnM_Uhy823qFSR7SoE

# Start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! ✅ Your bot is working.")

# Main function
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()
