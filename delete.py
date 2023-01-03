import os


os.chdir(os.path.dirname(__file__))


def remover(message):
    result = message.text
    with open('book.txt', 'r', encoding='utf-8') as file:
        file = list(map(str, file.read().split('\n')))
    content = [i for i in file if result not in i]
    with open('book.txt', 'w', encoding='utf-8') as file:
        for i in range(len(content)):
            file.write(content[i] + '\n')
    return 'Удалено!'
