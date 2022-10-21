from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет! {update.effective_user.first_name}!')

async def text_editing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    a = " ".join(list(filter(lambda x: 'абв' not in x, msg.split())))
    await update.message.reply_text(f'{a}')