import telebot
import settings
import example

from telebot import types

token_file = open('data/token.txt')
bot = telebot.TeleBot(token_file.readline())

@bot.message_handler(commands=['start'])

def start_dialogue_message(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item_en = example.draw_button("English")
    item_ru = example.draw_button("Russian")
    item_fr = example.draw_button("France")
    item_sp = example.draw_button("Spanish")
    item_zh = example.draw_button("China")
    item_jp = example.draw_button("Japan")

    markup_reply.add(item_en, item_ru, item_fr, item_sp, item_zh, item_jp)

    bot.send_message(message.chat.id, "Привет, {0.full_name}! Можешь начинать пользоваться ботом для перевода. Чтобы поменять язык используй кнопки снизу!".format(message.from_user), reply_markup=markup_reply)
    settings.enabled = True

@bot.message_handler(content_types = ['text'])

def translate_message(message) -> settings.enabled:
    language_settings(message)
    if message.text[0] != '/': 
        bot.send_message(message.chat.id, example.Translate(message.text))

def language_settings(message):
    match message.text:
        case 'English':
            settings.translate_language = 'en'
        case 'Russian':
            settings.translate_language = 'ru'
        case 'France':
            settings.translate_language = 'fr'
        case 'Spanish':
            settings.translate_language = 'es'
        case 'China':
            settings.translate_language = 'zh-tw'
        case 'Japan':
            settings.translate_language = 'ja'

def delete_markup_message(name, call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"Новый язык {name}", reply_markup=None)


bot.polling(none_stop=True)