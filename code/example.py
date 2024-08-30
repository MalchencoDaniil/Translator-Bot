from googletrans import Translator
import settings

from telebot import types

translator = Translator()

def download_audio_file(bot, file_id):
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    filename = file_id + file_info.file_path

    filename = filename.replace ('/', '')
    filename = filename.replace('.oga', '.wav')

    folder_path = f'AudioTranscriber/Audio/{filename}'

    with open(folder_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    return filename

def Translate(text):
    result = translator.translate(text, dest=settings.translate_language)
    return result.text

def draw_button(name):
    return types.KeyboardButton(name)