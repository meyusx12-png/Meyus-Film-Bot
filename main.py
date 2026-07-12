import os
from omdb import get_random_movie
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        async def film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_random_movie()

    if data.get("Response") == "False":
        await update.message.reply_text("Film bulunamadı.")
        return

    text = f"""
🎬 Meyus Film

🍿 {data['Title']}

⭐ IMDb: {data['imdbRating']}
📅 {data['Year']}
🎭 {data['Genre']}
⏱️ {data['Runtime']}

📝 {data['Plot']}

🎥 İyi seyirler!
"""

    if data["Poster"] != "N/A":
        await update.message.reply_photo(photo=data["Poster"], caption=text)
    else:
        await update.message.reply_text(text)

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