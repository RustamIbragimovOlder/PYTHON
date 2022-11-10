from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import datetime
from pytube import YouTube
import requests
from telegram import Bot

# Функция приветствия
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!\nЯ твой ТелеБот.\nДля просмотра списка моих функций введи /help')

# Функция вывода основного перечня функций
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Сейчас я могу реализовать следующие функции:\n/hi\n/time\n/help\n/calc\n/edit\n/game\n/download\n/viewing\n/valute')

# Функция вывода текущего времени
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Текущее время: {datetime.datetime.now().time()}')

# Функция вывода перечня функций калькулятора
async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/sum\n/sub\n/mult\n/div\n/exp')

# Функция сложения 2-х чисел
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')

# Функция вычитания 2-х чисел
async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

# Функция умножения 2-х чисел
async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')

# Функция деления 2-х чисел
async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')

# Функция возведения в степень
async def exp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ** {y} = {x ** y}')

# Функция редактирования текста
async def edit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    a = " ".join(list(filter(lambda x: 'абв' not in x, msg.split())))
    await update.message.reply_text(f'{a}')

# Функция скачивания видео из Ютуб по ссылке
async def video_download_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split()[1]
    yt = YouTube(url)
    yt.streams.filter(res="360p").first().download(filename=f"{yt.title}.mp4")
    # print(yt.title)

# Функция просмотра загруженного видео из Ютуб
async def video_viewing_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# def video_viewing_command(update:..., context:..., bot: <--- тут еще аттрибут понадобится, чтобы видеть его в функции):
    data = update.message.text.split()[1]
    # await msg.send_video(chat_id = 894667527, video=open(data, 'rb'))
    # await update.bot.send_video(update.chat_id, video=open('update.message.chat.id.mp4', 'rb'))
    # await bot.send_video(update.message.chat.id, update.message.chat.id.mp4)
    # await update.message.reply_text(f'{yt.title}')
    # await update.bot.send_document(chat_id = chat_id chat_id, document='https://python-telegram-bot.org/static/testfiles/telegram.gif'))
    # await bot.send_video(chat_id = 894667527, video=open('update.message.chat.id.mp4', 'rb'))
    # await bot.send_video(chat_id = 894667527, video=open('894667527.mp4', 'rb'))
    # bot = Bot(token="TOKEN")
    # await bot.send_video(chat_id = 894667527, video=open('C:\Users\Рустам Ибрагимов\repositories\PYTHON\Tobias Rauscher - Passion Loop (ORIGINAL).mp4', 'rb'))
    # await messages.sendMedia(chat_id = 894667527, video=open(data, 'rb'))
    # await update.message.sendMedia(chat_id = 894667527, video=open(data, 'rb'))
    await update.message.reply_video(media=data)

  

# Функция выбора валюты
async def valute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Выбери валюту:\n/GBP\n/BYN\n/USD\n/EUR\n/CNY\n/JPY')
    await update.message.reply_text(f'Введи /type и код валюты')

# Функция получения актуального курса валюты
async def well_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    currency_type = update.message.text.split()[1]
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    nominal = data['Valute'][currency_type]['Nominal']
    name = data['Valute'][currency_type]['Name']
    value = data['Valute'][currency_type]['Value']
    await update.message.reply_text(f'{nominal} {name} => {value} руб.')






