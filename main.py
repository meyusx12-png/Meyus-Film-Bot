import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Merhaba! Ben Meyus Film Bot.\n\n"
        "Şimdilik test sürümündeyim.\n"
        "/film komutu yakında aktif olacak."
    )

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍿 Bugünün filmi: Interstellar (2014)\n⭐ IMDb: 8.7"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("film", film))

    print("Meyus Film Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()