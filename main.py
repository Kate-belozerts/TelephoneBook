'''Прикрутить бота: Создать телефонный справочник с 
возможностью импорта и экспорта данных в нескольких форматах.'''
from telebot import TeleBot, types
import os
import find
import add
import delete
os.chdir(os.path.dirname(__file__))


#https://t.me/TelephonebookbookbookBot
TOKEN = '5776646199:AAFsIF6UI_URyev2MtqPppolYci7oD6iru8'


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def answer(msg: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
                types.InlineKeyboardButton(text='Найти номер', callback_data='1'),
                types.InlineKeyboardButton(text='Добавить контакт', callback_data='2') )
    keyboard.row(types.InlineKeyboardButton(text='Удалить контакт', callback_data='3') )
    keyboard.row(
                types.InlineKeyboardButton(text='Файл со всеми данными', callback_data='4'),
                types.InlineKeyboardButton(text='Импортировать файл', callback_data='5') )

    bot.send_message(msg.from_user.id, text='Действия с телефонной книгой: ', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == '1')  # НАЙТИ НОМЕР
def call_back1(call):
    bot.send_message(chat_id=call.from_user.id, text='Введите номер или имя, которое хотите найти:')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(msg):
        result = find.next_step(msg)
        bot.reply_to(msg, text=f'{result}')


@bot.callback_query_handler(func=lambda call: call.data == '2')  # ДОБАВИТЬ НОМЕР
def call_back2(call):
    bot.send_message(chat_id=call.from_user.id, text='Введите без пробелов имя, фамилию, номер телефона и комментарий через ";" ')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(msg):
        result = add.new_contact(msg)
        bot.reply_to(msg, text=f'{result}')


@bot.callback_query_handler(func=lambda call: call.data == '3')  # УДАЛИТЬ НОМЕР
def call_back3(call):
    bot.send_message(chat_id=call.from_user.id, text='Введите номер или имя контакта, который хотите удалить')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(msg):
        result = delete.remover(msg)
        bot.reply_to(msg, text=f'{result}')


@bot.callback_query_handler(func=lambda call: call.data == '4')  # ОТПРАВИТЬ КНИЖКУ ФАЙЛОМ
def call_back4(call):
    bot.send_message(chat_id=call.from_user.id, text='Ок. Отправляю текстовым файлом все ваши номера')
    f = open('book.txt', 'rb')
    bot.send_document(call.from_user.id, f)
    f.close()


@bot.callback_query_handler(func=lambda call: call.data == '5')  # ИМПОРТ ФАЙЛА ВО ВНУТРЕННИЙ
def call_back5(call):
    bot.send_message(chat_id=call.from_user.id, text='Ок. Отправьте файл, я добавлю всё из него в вашу записную книжку')

    @bot.message_handler(content_types=['document'])
    def download(msg):
        file_info = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        name = 'book.txt'
        with open(name, 'ab') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(msg, text='Готово!')


bot.polling()
