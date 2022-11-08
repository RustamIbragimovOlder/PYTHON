from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import *


app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("text_ed", text_editing))

print('server start')
app.run_polling()