import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Token environment variable se lo (Render me set karna hai)
TOKEN = os.getenv("8208891679:AAE6j5aVkxE8SsAJyLnM_Uhy823qFSR7SoE")

# Start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is live and working!")

# Main function
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
