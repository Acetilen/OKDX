import telebot ############!!!!!!!!!!!Сюда же пилим для баллов на конкурсах
from telebot import types
import time
import re
from s import token
import sqlite3

def escape_markdown(text): # экранирует markdown
    escape_chars = r'[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

def make_a_db():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY,
                    acces_level INTEGER,
                    points INTEGER  
                )
                ''')
    connection.commit()
    connection.close()



def db_add(id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute()

make_a_db()

bot = telebot.TeleBot(token)

def botik():
    try:
        @bot.message_handler(commands = ['start','go'])
        def start_go_message(message):
            global users
            user_id = message.from_user.id
            if user_id not in list(users.keys()):
                users.update({str(user_id):()})
                print(users)
            match message.text:
                case "/start":
                    bot.send_message(user_id, escape_markdown("*Привет!*👋\nЯ бот ОКДХ БГУ, через меня можно забронировать билеты на концерт, с помощью команды */go*"), parse_mode="markdownv2")
                case "/go":
                    bot.send_game(user_id, "DX_tickets")
                case "/help":
                    bot.send_message(user_id, escape_markdown("Лови список тех команды которые я знаю:\n */go* - я помогу тебе забронировать билеты на концерт\n */help* - ты получишь это сообщение"), parse_mode="markdownv2")
                case _:
                    bot.send_message(user_id, escape_markdown("Такой команды у меня пока нет\n Вот список команд которые мне знакомы:\n */go* - я помогу тебе забронировать билеты на концерт\n */help* - ты получишь это сообщение"), parse_mode="markdownv2")

        @bot.callback_query_handler(func = lambda callback_query: callback_query.game_short_name == "DX_tickets")
        def game(call):
            bot.answer_callback_query(callback_query_id=call.id, url = "https://onliner.by/")


        bot.polling(none_stop=True, interval = 0)
    except:
        print("Бот умер!")
        time.sleep(1)
        botik()

botik()

{user_id: (5, 8)}