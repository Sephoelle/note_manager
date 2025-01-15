username = input('Введите имя: ')
title1 = input('Введите заголовок: ')
title2 = input('Введите заголовок: ')
title3 = input('Введите заголовок: ')
content = input('Введите содержание заметки: ')
status = input('Статус заметки: ')
create_date = str(input('Дата создания заметки в формате "дд.мм.гггг": '))
issue_date = str(input('Дата истечения заметки в формате "дд.мм.гггг": '))

note = [username,
        [title1, title2, title3],
        content,
        status,
        create_date[:5],
        issue_date[:5]]

print(note)