from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import datetime

# Функция приветствия
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет! {update.effective_user.first_name}!\nЯ твой ТелеБот.\nДля просмотра списка моих функций введи /help')

# Функция вывода текущего времени
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Текущее время: {datetime.datetime.now().time()}')

# Функция вывода основного перечня функций
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Сейчас я могу реализовать следующие функции:\n/hi\n/time\n/help\n/calc\n/edit\n/game')

# Функция вывода перечня функций калькулятора
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/sum\n/sub\n/mult\n/div\n/exp')

# Функция сложения 2-х чисел
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

# Функция вычитания 2-х чисел
async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

# Функция умножения 2-х чисел
async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')

# Функция деления 2-х чисел
async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')

# Функция возведения в степень
async def exp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ** {y} = {x ** y}')

# Функция редактирования текста
async def edit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    a = " ".join(list(filter(lambda x: 'абв' not in x, msg.split())))
    await update.message.reply_text(f'{a}')
