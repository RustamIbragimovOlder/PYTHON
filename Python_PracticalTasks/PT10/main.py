from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bots_commands import *
from game_progress import *

app = ApplicationBuilder().token("MY TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("exp", exp_command))
app.add_handler(CommandHandler("edit", edit_command))
app.add_handler(CommandHandler("game", game_command))
app.add_handler(CommandHandler("draw", draw_command))
app.add_handler(CommandHandler("s", start_game))
app.add_handler(CommandHandler("video", video_command))
app.add_handler(CommandHandler("valute", valute_command))
app.add_handler(CommandHandler("type", well_command))

print('server start')
app.run_polling()


