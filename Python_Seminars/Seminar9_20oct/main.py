from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import *


app = ApplicationBuilder().token("5715548573:AAFHStsDcP_U9tfw_99Yguoic-4BN-Eo4VM").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("text_ed", text_editing))

print('server start')
app.run_polling()