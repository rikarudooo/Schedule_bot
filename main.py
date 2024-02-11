import re
import csv

from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler, Updater

##Isi Token dari Telegram Bot
token =

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Halo. Selamat datang di bot My Activity. Bot ini akan memberikan aktivitasmu."
    )

async def tanggal(update:Update, context:ContextTypes.DEFAULT_TYPE):
    input_data = "request anda berhasil"
    data = update.message.text

    input = re.search(r'\d+.*', data).group()
    ## Sampel format menggunakan dd-mm-yyyy
    if len(input) != 10:
        input_data = "Your input should be like 01-01-95 (DD-MM-YYYY)"
    else:
        input_date = input.split("-")
        day = input_date[0]
        month = input_date[1]
        year = input_date[2]

        file_path = 'source.csv'
        data = [
            ["day", "month", "year"],
            [day, month, year]
        ]
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=input_data
    )

if __name__ == "__main__":
    application = Application.builder().token(token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    tanggal_handler = CommandHandler('tanggal', tanggal)
    application.add_handler(tanggal_handler)

    application.run_polling()

## Test boy
