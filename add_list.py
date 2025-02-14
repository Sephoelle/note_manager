# Собираем данные от пользователя с помощью "input(__prompt)"

username = input('Введите имя: ')
title1 = input('Введите заголовок: ')
title2 = input('Введите заголовок: ')
title3 = input('Введите заголовок: ')
title_list = [title1.capitalize(), title2.capitalize(), title3.capitalize()] # Объединяем несколько заголовков в список
content = input('Введите содержание заметки: ')
status = input('Статус заметки: ')
create_date = str(input('Дата создания заметки в формате "дд.мм.гггг": '))
issue_date = str(input('Дата истечения заметки в формате "дд.мм.гггг": '))

# Вывод данных

print('Имя пользователя:', username)
print('Заголовок:', end=' ')
print(*title_list, sep='. ', end='.\n')
print('Описание:', content)
print('Статус:', status)
print('Дата создания:', create_date[:5])
print('Дата истечения:', issue_date[:5])
