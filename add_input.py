# Добавляем функцию input(__prompt) для сбора данных от пользователя

username = input('Введите имя: ')
title = input('Введите заголовок: ')
content = input('Введите содержание заметки: ')
status = input('Статус заметки: ')
create_date = str(input('Дата создания заметки в формате "дд.мм.гггг": '))
issue_date = str(input('Дата истечения заметки в формате "дд.мм.гггг": '))

# Вывод данных

print('Имя пользователя:', username)
print('Заголовок:', title)
print('Описание:', content)
print('Статус:', status)
print('Дата создания:', create_date[:5])
print('Дата истечения:', issue_date[:5])