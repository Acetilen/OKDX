import telebot
from telebot import types
from s import token

bot = telebot.TeleBot(token)
# Делаем херню для выбора мест монжо матрицей
# Людей храним в дб? или в json
# Соответственно поиск и запись человека 

@bot.message_handler(commands = ['start'])
def start_message(message):
    user_id = message.from_user.id
    bot.send_game(user_id, "DX_tickets")

@bot.callback_query_handler(func = lambda callback_query: callback_query.game_short_name == "DX_tickets")
def game(call):
    bot.answer_callback_query(callback_query_id=call.id, url = "https://agar.io/")

bot.polling(none_stop=True, interval = 0)