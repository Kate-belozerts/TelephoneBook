import os


os.chdir(os.path.dirname(__file__))


def next_step(message):
    result = message.text
    with open('book.txt', 'r', encoding='utf-8') as file:
        content = list(map(str, file.read().split('\n')))
    temp = []
    for j in content:
        if result in j:
            temp.append(j)
    if len(temp) == 0:
        return 'Ничего не найдено!'
    else:
        res = '' + temp[0]
        return res.replace(';', ' ')
