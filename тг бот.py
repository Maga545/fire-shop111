import random
import telebot
import webbrowser
from telebot import types

file = open('./mytoken.txt')
mytoken = file.read()
bot = telebot.TeleBot(mytoken)
answers = ['Файр не может тебя понять', 'Я не понял-_-', 'Я не знаю такой команды.', 'Мой создаватель не говорил, что отвечать в такой ситуации >_<']


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Каталог')
    button2 = types.KeyboardButton('⚙️ Настройки')
    button3 = types.KeyboardButton('📄 Информация')

    markup.row(button1)
    markup.row(button2, button3)

    if message.text == '/start':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nЗдесь ты сможешь купить цифровые товары!\nКонтакт моего разработчика: https://t.me/designfromfire', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Теперь ты в главном меню, выбирай!', reply_markup=markup)


@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'Я не могу смотреть картинки(')


@bot.message_handler()
def info(message):
    if message.text == '🛍 Каталог':
        goodsChapter(message)
    elif message.text == '⚙️ Настройки':
        settingsChapter(message)
    elif message.text == '📄 Информация':
        koshelkuTop(message)
    elif message.text == 'Документы📃':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о втором товаре...', reply_markup=markup)
    elif message.text == 'Услуги🦾':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о третьем товаре...', reply_markup=markup)
    elif message.text == 'Оформление🖌':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о четвертом товаре...', reply_markup=markup)
    elif message.text == '⚙️ Настройки #1':
        # Функционал не придумал
        bot.send_message(message.chat.id, 'Настройки номер 1...')
    elif message.text == '⚙️ Настройки #2':
        # Функционал не придумал
        bot.send_message(message.chat.id, 'Настройки номер 2...')
    elif message.text == '💳 Купить' or message.text == '✏️ Написать разработчику':
        webbrowser.open('https: //t.me/designfromfire')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    elif message.text == 'Кошельки👛':
        koshelkuTop(message)
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])


def goodsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Кошельки👛')
    button2 = types.KeyboardButton('Документы📃')
    button3 = types.KeyboardButton('Услуги🦾')
    button4 = types.KeyboardButton('Оформление🖌')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Вот все категории в продаже:', reply_markup=markup)


def koshelkuTop(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Qiwi🥝')
    button2 = types.KeyboardButton('Youmoney💜')
    button3 = types.KeyboardButton('Lava🌋')
    button4 = types.KeyboardButton('Binance🥇')
    button5 = types.KeyboardButton('↩️ Назад')
    markup.row(button1, button2, button3, button4)
    markup.row(button5)

def settingsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('⚙️ Настройки #1')
    button2 = types.KeyboardButton('⚙️ Настройки #2')
    button3 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Раздел настроек\nВыбери один из вариантов:', reply_markup=markup)


def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Раздел информации\nЗдесь ты можешь написать моему разработчику.', reply_markup=markup)




bot.polling(none_stop=True)
