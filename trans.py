import telebot
from translate import Translator

TOKEN = 'ВАШ ТОКЕН'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(func=lambda message: True)
def function_name(message):
    try:
        a1 = message.text
        translator = Translator(from_lang='Russian', to_lang='English')
        translation = translator.translate(a1)
        print(translation)
        a2 = message.from_user.username
        # with open('data.txt', 'a') as file:
        #     file.write(f'@{a2} написал: {a1}\n')
        bot.reply_to(message, f"{translation}")
    except RuntimeError:
        bot.reply_to(message, f"{message.from_user.username}, слова нет в базе данных")
bot.infinity_polling()
