import os
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Берём токен и ID из переменных окружения
TOKEN = os.getenv("TOKEN")
MY_ID = int(os.getenv("MY_ID"))

bot = Bot(token=TOKEN)

async def start(update: Update, context):
    await update.message.reply_text("Привет! Отправляй сообщения анонимно.")

async def echo(update: Update, context):
    text = update.message.text
    photo_list = update.message.photo
    caption = update.message.caption

    if photo_list:
        photo = photo_list[-1]
        file_id = photo.file_id
        final_caption = f"Анонимное сообщение: {caption}" if caption else "Анонимное фото"
        await bot.send_photo(chat_id=MY_ID, photo=file_id, caption=final_caption)

    elif text:
        msg = f"Анонимное сообщение: {text}"
        await bot.send_message(chat_id=MY_ID, text=msg)

    await update.message.reply_text("Сообщение отправлено анонимно!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, echo))

app.run_polling()