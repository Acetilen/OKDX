import telebot ############!!!!!!!!!!!Сюда же пилим для баллов на конкурсах
from telebot import types
import time
import re
from s import token
import sqlite3

def escape_markdown(text): # экранирует markdown
    escape_chars = r'[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

bot = telebot.TeleBot(token)

places = {
    1 : {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0},
    2 : {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0},
    3 : {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0},
    4 : {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0},
    5 : {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0},
    6 : {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    }



# @bot.message_handler(commands = ['start','go'])
# def start_go_message(message):
#     user_id = message.from_user.id
#     if user_id not in list(users.keys()):
#         users.update({str(user_id):()})
#         print(users)
#     match message.text:
#         case "/start":
#             bot.send_message(user_id, escape_markdown("*Привет!*👋\nЯ бот ОКДХ БГУ, через меня можно забронировать билеты на концерт, с помощью команды */go*"), parse_mode="markdownv2")
#         case "/go":
#             bot.send_game(user_id, "DX_tickets")
#         case "/help":
#             bot.send_message(user_id, escape_markdown("Лови список тех команды которые я знаю:\n */go* - я помогу тебе забронировать билеты на концерт\n */help* - ты получишь это сообщение"), parse_mode="markdownv2")
#         case _:
#             bot.send_message(user_id, escape_markdown("Такой команды у меня пока нет\n Вот список команд которые мне знакомы:\n */go* - я помогу тебе забронировать билеты на концерт\n */help* - ты получишь это сообщение"), parse_mode="markdownv2")

# bot.polling(none_stop=True, interval = 0)


