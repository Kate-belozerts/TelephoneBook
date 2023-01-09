'''Прикрутить бота: Создать телефонный справочник с 
возможностью импорта и экспорта данных в нескольких форматах.'''
quit()
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

# Other
# key_5 = types.InlineKeyboardButton(text='Импортировать файл', callback_data='5')
# keyboard.add(key_5)
# __________________________________________________________________________
# @bot.callback_query_handler(func=lambda call: True)
# def call_back(call):
#     if call.data == '1':
#         # bot.send_message(call.from_user.id, text='Введите номер')
#         @bot.message_handler(content_types=['text'])
#         def get_text_messages(msg):
#             bot.send_message(chat_id=msg.from_user.id, text='Введите номер')


# ________________________________________________________________________________________________
#     @bot.callback_query_handler(func=lambda call: call.data == 'yes')
#     def call_back(call):
#         bot.send_message(chat_id=call.from_user.id, text='Хорошо, давайте продолжим?')

#         @bot.message_handler(content_types=['text'])
#         def get_text_messages(msg):
#             bot.send_message(chat_id=msg.from_user.id, text='Нужно ввести арифметическое выражение: \n\
# (Возведение в степень укажите как "^", а корень словом "root")\n')
#             bot.register_next_step_handler(msg, start)

#     @bot.callback_query_handler(func=lambda call: call.data == 'no')
#     def call_back(call):
#         bot.send_message(chat_id=call.from_user.id, text=f'Хорошо, закончим на сегодня. До свидания!)')


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.register_next_step_handler(message, start)


#___________________________________________КНОПКА!________________________________________________________

    # bot.send_message(chat_id=call.from_user.id, text='Ок. Отправьте любое сообщение. Без этого кнопки не работают, чтоб их')
    # @bot.message_handler(content_types=['text'])
    # def get_text_messages(msg):
    #     bot.send_message(chat_id=msg.from_user.id, text='Введите номер или имя, которое хотите найти:')
    #     result = find.next_step(msg)
    #     bot.reply_to(msg, text=f'{result}')
    #     bot.register_next_step_handler(msg, answer)

#____________________________________________________________________-
        # name = 'book.txt' # + msg.document.file_name
#_________________________________Удалить кнопки после нажатия______________________________________________________________
        # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
