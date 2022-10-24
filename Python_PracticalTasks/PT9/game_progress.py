from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint

# Функция вывода этапов игры
async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/draw\n/start')

# Функция жеребьевки
async def draw_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Давай сыграем!\nУсловия игры:\n На столе лежит 2021 конфета.\nДелаем ходы по очереди.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты достаются сделавшему последний ход.')
    await update.message.reply_text(f'Проводим жеребьевку. Кидаем кубик:')
    A = randint(1, 6)
    B = randint(1, 6)
    await update.message.reply_text(f'Оп!\nТебе выпало => {A}\nМне выпало => {B}')
    if A == B:
        await update.message.reply_text(f'У нас одинаковое число!\nПовторяем жеребьевку\nОпять набери /draw')
    else:
        if A > B:
            await update.message.reply_text('У тебя больше\nПервый ход твой')
            await update.message.reply_text(f'Начинаем игру.\nНабери /s и количество конфет')
        elif A < B:
            await update.message.reply_text('У меня больше\nПервый ход мой')
            await update.message.reply_text(f'Начинаем игру.')
            y = randint(1, 28)
            await update.message.reply_text(f'Я беру {y} конфет')
            b = number_candies[len(number_candies) - 1]
            b -= y
            number_candies.append(b)
            await update.message.reply_text(f'На столе осталось {b} конфет\nТвой ход\nНабери /s и количество конфет')

number_candies = [2021]

# Функция игры 
async def start_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    b = number_candies[len(number_candies) - 1]
    msg = update.message.text
    items = msg.split()
    a = int(items[1])
    b -= a
    await update.message.reply_text(f'Ты взял {a} конфет.\nНа столе осталось {b} конфет')
    number_candies.append(b)
    print(number_candies)
    if b == 0:
        await update.message.reply_text(f'Конфеты кончились.\nМолодец! Ты выиграл!\nЧтоб у тебя ж... слиплась')
        await update.message.reply_text(f'Для новой игры необходимо перезапустить скрипт в VSCode')
    else:
        if b > 28:
            y = randint(1, 28)
            await update.message.reply_text(f'Я беру {y} конфет')
            b -= y
            await update.message.reply_text(f'На столе осталось {b} конфет\nТвой ход\nНабери /s и количество конфет')
        else:
            await update.message.reply_text(f'Я беру {b} конфет.\nКонфеты кончились.\nТы проиграл!\nО! Как вкусно')
            await update.message.reply_text(f'Для новой игры необходимо перезапустить скрипт в VSCode')

    number_candies.append(b)


