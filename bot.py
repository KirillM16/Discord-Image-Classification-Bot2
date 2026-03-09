import telebot
from logic import detect_bird
bot = telebot. TeleBot('*******')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот.")

@bot.message_handler(content_types=['photo'])
def get_photo(message) :
    print (message)
    bot.send_message(message.chat.id, 'Ваше фото принято!Начинается обработка...')
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open('img/' + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    name, acc = detect_bird('img/' + file_name)
    bot.send_message(message.chat.id, f'На фото: {name}')
bot.polling()