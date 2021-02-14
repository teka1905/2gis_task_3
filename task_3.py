import re
import os.path
import time

while True:
    file_path = input('Enter the path to the file: ')
    if os.path.isfile(file_path):
        break
    else:
        print('The path is incorrect, please try again')
        time.sleep(1)

path = open(file_path, 'r', encoding='utf-8').read().lower()
search_word = input(str('Enter your search word: '))
count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(search_word.lower()), path))

print('The word', search_word, 'occurs', count, 'times in the file.')
time.sleep(5)
