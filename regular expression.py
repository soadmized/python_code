import re

password = input('Введите строку:')
exp = re.compile('[а-яА-ЯёЁ]')
if exp:
    print("В стороке есть буквы")
else:
    print('В строке нет букв')
