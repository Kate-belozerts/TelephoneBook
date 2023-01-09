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
 
 
def send_menu(msg):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
                types.InlineKeyboardButton(text='Найти номер', callback_data='1'),
                types.InlineKeyboardButton(text='Добавить контакт', callback_data='2'))
    keyboard.row(types.InlineKeyboardButton(text='Удалить контакт', callback_data='3'))
    keyboard.row(
                types.InlineKeyboardButton(text='Файл со всеми данными', callback_data='4'),
                types.InlineKeyboardButton(text='Импортировать файл', callback_data='5'))
 
    bot.send_message(msg.chat.id, text='Действия с телефонной книгой: ', reply_markup=keyboard)
 
 
@bot.message_handler(commands=['start'])
def answer(msg: types.Message):
    send_menu(msg)

 
@bot.callback_query_handler(func=lambda call: True)
def call_back1(call: types.CallbackQuery):
    new_text = '_'
    if call.data == '1':
        new_text = 'Введите номер или имя, которое хотите найти:'
        bot.register_next_step_handler(call.message,  find_step)
    elif call.data == '2':
        new_text = 'Введите без пробелов имя, фамилию, номер телефона и комментарий через ";" '
        bot.register_next_step_handler(call.message, new_contact_step)
    elif call.data == '3':
        new_text = 'Введите номер или имя контакта, который хотите удалить'
        bot.register_next_step_handler(call.message, remove_step)
    elif call.data == '4':
        new_text = 'Ок. Отправляю текстовым файлом все ваши номера'
        with open('book.txt', 'rb') as f:
            bot.send_document(call.from_user.id, f)
        send_menu(call.message)
    elif call.data == '5':
        new_text = 'Ок. Отправьте файл, я добавлю всё из него в вашу записную книжку'
        bot.register_next_step_handler(call.message, download_step)
 
    bot.edit_message_text(chat_id=call.from_user.id,message_id=call.message.id,
                          text=new_text, reply_markup=None)
 
 
def find_step(msg):
    result = find.next_step(msg)
    bot.reply_to(msg, text=f'{result}')
    send_menu(msg)
 
 
def new_contact_step(msg):
    result = add.new_contact(msg)
    bot.reply_to(msg, text=f'{result}')
    send_menu(msg)
 
 
def remove_step(msg):
    result = delete.remover(msg)
    bot.reply_to(msg, text=f'{result}')
    send_menu(msg)
 
 
def download_step(msg):
    file_info = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
 
    name = 'book.txt'
    with open(name, 'ab') as new_file:
        new_file.write(downloaded_file)
 
    bot.reply_to(msg, text='Готово!')
    send_menu(msg)


bot.polling()
