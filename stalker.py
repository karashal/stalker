#!/usr/bin/python
# -*- coding: utf-8 -*-

# The script for deleting Cyrillic saves in the game S.T.A.L.K.E.R.

# Import os to work with files.
import os

# Cyrillic alphabet.
LETTERS = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
		 		'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
		 		'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')

# Path to save game. Something like that...
SAVES = r'D:\Games\S.T.A.L.K.E.R. - Объединенный Пак 2\appdata\savedgames'

# Open the file.
for top, dirs, files in os.walk(SAVES):
	print(f'Total number of files - {len(files)}.')
	for file in files:
		
		# Checking files for Cyrillic.
		for letter in LETTERS:
			if letter in file:

				# If the file is in Cyrillic, then delete it.
				print(f'{file} - deleted.')
				os.remove(os.path.join(SAVES, file))
				break
