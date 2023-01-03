import os


os.chdir(os.path.dirname(__file__))


def new_contact(message):
    result = message.text
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(result)
        file.write('\n')
    return 'Готово!'
