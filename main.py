import random
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
bot = telebot.TeleBot("5357647506:AAGieA1lGVe0Uv8BXuxV4erk0_fZlB9yfC8")

# def markup_inline():
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton("Інлайнкнопка", callback_data="56"))
#     markup.add(InlineKeyboardButton("Музка", callback_data="Музика"))
#
#     return markup
#
#
# @bot.message_handler(commands=['gospody'])
# def send_welcome(message):
#     markup = ReplyKeyboardMarkup(row_width=4)
#     itembtn1 = KeyboardButton('Пісня 1')
#     itembtn2 = KeyboardButton('Пісня 2')
#     itembtn3 = KeyboardButton('Пісня 3')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.reply_to(message, "Вибери пісню:", reply_markup=markup)
#
# @bot.message_handler(content_types=['text'])
# def conversation(message):
#     if message.text == "Пісня 1":
#         bot.send_message(message.chat.id, "Червона рута")
#     if message.text == "Пісня 2":
#         bot.send_message(message.chat.id, "Smells like teen spirit")
#     if message.text == "Пісня 3":
#         bot.send_message(message.chat.id, "Hot&Cold")
#     else:
#         bot.send_message(message.chat.id, "Тут інлайн кнопка", reply_markup=markup_inline())
#         # bot.send_video(message.chat.id, "https://www.youtube.com/watch?v=-B72XUki4pM")
#
# @bot.callback_query_handler(func=lambda call: True)   #ця функція робить дію на натискання інлайн кнопки
# def callback_query(call):
#     if call.data == "56":
#         # bot.send_message(call.from_user.id, "Valeriia")
#         bot.answer_callback_query(call.id, "Котик-муркотик")
#     if call.data == "Музика":
#         bot.send_message(call.from_user.id, "ЛЯляля")
#
#
# bot.polling(none_stop=True)
# # age = 16
# # while True:
# #
# #     age -= 1
# #     print("Hello", age )
# #     if age == 12:
# #         break
# #

img = [
    'https://bit.ly/3yP4Ya8',
    'https://bit.ly/3CLkzZo',
    'https://bit.ly/3S5qLBj',
    'https://bit.ly/3eJkCx2',
    'https://bit.ly/3ghQY2g',
    'https://cutt.ly/JB8OQPK',
    'https://cutt.ly/MB8OOYf',
    'https://cutt.ly/3B8OKHv',
    'https://cutt.ly/rB8O1Ho'
]
#     'https://cutt.ly/vB8O3UK',
#     'https://cutt.ly/WB8O6R1' два невалідних посилання, на які видає помилку
wishes = [
    'Нехай у твоєму сьогоднішньому дні буде тільки солодка начинка, яка припала б до смаку!',
    'Бажаю тобі, щоб цей день став початком довгої низки з приємних і тривалих моментів в житті!',
    'Нехай сьогодні всі мрії здійсняться, а удача, з ранку постукавши у двері, вже ніколи тебе не залишить. Прокидайся, зустрічай і хапай її, проказницу, за хвіст. Гарного тобі дня.',
    'Немає слів, щоб показати, як мені хочеться, щоб кожен твій день був добрим і погожим. Бажаю сонця в небі і спокою на душі!',
    'Бажаю тобі невичерпної енергії на весь день і щоб все задумане виходило з першого разу!',
    'Бажаю весь день посмішки оточуючим дарувати і ні в якому разі не хандрити!',
]


@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id,'Привіт, цей бот буде присилати тобі кожен день по мавпочці, яка буде описувати твій наступний день :)', reply_markup=button(message))
     while True:
         bot.send_photo(message.chat.id, random.choice(img))
         bot.send_message(message.chat.id, random.choice(wishes))
         time.sleep(60)

@bot.message_handler(content_types=['text'])
def button(message):
    markup = ReplyKeyboardMarkup(row_width=1)
    itembtn1 = KeyboardButton('Хочу ще мавпочку)')
    itembtn2 = KeyboardButton('Хочу ще побажань')
    markup.add(itembtn1,itembtn2)
    bot.reply_to(message, "Можеш вибрати додаткові дії:", reply_markup=markup)
    return markup
# def murkup_inline():
#      markup = InlineKeyboardMarkup()
#      markup.add(InlineKeyboardButton('Така ти мавпа зараз', callback_data="1"))
#      return markup

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Хочу ще мавпочку)':
        bot.send_message(message.chat.id, "Виберіть автора пісніg", reply_markup=markup_autors())
        bot.send_photo(message.chat.id, random.choice(img))
    elif message.text == 'Хочу ще побажань':
        bot.send_message(message.chat.id, random.choice(wishes))

bot.polling(none_stop=True)

