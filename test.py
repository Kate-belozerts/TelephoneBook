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
