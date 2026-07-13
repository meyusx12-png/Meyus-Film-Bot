import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from tmdb import get_random_movie

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Merhaba! Ben Meyus Film Bot.\n\n"
        "/film yazarak film önerisi alabilirsin."
    )

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_random_movie()

    if data.get("Response") == "False":
        await update.message.reply_text("Film bulunamadı.")
        return

    text = (
        f"🎬 {data['Title']}\n\n"
        f"⭐ IMDb: {data['imdbRating']}\n"
        f"📅 Yıl: {data['Year']}\n"
        f"🎭 Tür: {data['Genre']}\n"
        f"⏱️ Süre: {data['Runtime']}\n\n"
        f"📝 {data['Plot']}"
    )

    if data["Poster"] != "N/A":
        await update.message.reply_photo(photo=data["Poster"], caption=text)
    else:
        await update.message.reply_text(text)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("film", film))

    print("Meyus Film Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()