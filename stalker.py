#!/usr/bin/python
# -*- coding: utf-8 -*-

# Скрипт для удаление сохранений на кириллице в игре S.T.A.L.K.E.R.
# Все информации об обновлении/ошибки, и инструкция в файле readme.txt.

import os

LETTERS = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
		 		'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
		 		'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')

# Путь к сохранениям.
SAVES = r'D:\Games\games_ready\S.T.A.L.K.E.R. - Объединенный Пак 2\appdata\savedgames'

# Открываем файлы.
for top, dirs, files in os.walk(SAVES):
	print(f'Общее количество файлов - {len(files)}.')
	for file in files:
		
		# Проверяем файлы на кириллицу.
		for letter in LETTERS:
			if letter in file:

				# Если файл на кириллице, тогда удаляем.
				print(f'{file} - удалена.')
				os.remove(os.path.join(SAVES, file))
				break

# Некорректно работает.
# print(f'Количество файлов после удаление - {len(files)}.')
