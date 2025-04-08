import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('اسمت رو بفرست تا سنت رو حدس بزنم!')


async def guess_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ass = update.message.text
    age = (len(ass) * 3) % 70
    await update.message.reply_text(f'{ass}، حدس من: {age} سال!')


def main():
    application = Application.builder().token("7654513264:AAFOCxSEOuv0BeYloaTdHmqSCfyoSsd4yiY").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess_age))

    application.run_polling()

if __name__ == '__main__':
    main()