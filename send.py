# import os
# from telebot import TeleBot, types
# os.chdir(os.path.dirname(__file__))


# TOKEN = '5776646199:AAFsIF6UI_URyev2MtqPppolYci7oD6iru8'
 
 
# bot = TeleBot(TOKEN)


# def send_file(msg):
#     if msg == '1':
#         return 'book.txt'

#     elif msg == '2':
#         with open('book.txt', 'r', encoding = 'utf-8') as file:
#             file = list(map(str, file))
#             with open('book.xlsx', 'w', encoding = 'utf-8') as new_file:
#                 new_file.writelines(file)
#                 return 'book.xlsx'


# print(type(send_file('1')))
# print(send_file('1'))

    # if msg == '1':
        # bot.send_message('Ок. Отправляю текстовым файлом все ваши номера')
        # with open('book.txt', 'r') as f:
            # bot.send_document(call.from_user.id, f)
    # elif msg == '2':
    #     # bot.send_message(f'Ок. Отправляю файлом {msg} все ваши номера')
    #     with open('book.txt', 'r', encoding = 'utf-8') as file:
    #         file = list(map(str, file))
    #         with open('book.xlsx', 'w', encoding = 'utf-8') as new_file:
    #             new_file.writelines(file)