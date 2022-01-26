import re

file_path = 'MOCK_DATA.txt'
surname_name = 'names'
mail = 'mail'
file_extension = 'file extension'
color_code = 'color code'

file_reader = open(file_path, mode='r', encoding='Latin-1')
surname_name = open(surname_name, mode='w', encoding='Latin-1')
mail = open(mail, mode='w', encoding='Latin-1')
file = open(file_extension, mode='w', encoding='Latin-1')
colour = open(color_code, mode='w', encoding='Latin-1')
text_file = file_reader.read()

what_to_search = r"[A-Z][a-z_-]+[\s][de\sA-Z'\s]+[a-zA-Z]+"
total = re.findall(what_to_search, text_file)
print(total)

for item in total:
    print(item)
    surname_name.write(item + '\n')

what_to_search = r'[\w_-]+@[\w_-]+.[\w.]+'
total = re.findall(what_to_search, text_file)
print(total)

for item in total:
    print(item)
    mail.write(item + '\n')

print(f'Total data of the file: {str(len(total))}')

what_to_search = r'[A-Z\s]+[a-zA-Z]+[.][a-z\d]+'
total = re.findall(what_to_search, text_file)
print(total)

for item in total:
    print(item)
    file.write(item + '\n')

print(f'Total data of the file: {str(len(total))}')

what_to_search = r'#[\d[a-z]\w+'
total = re.findall(what_to_search, text_file)
print(total)

for item in total:
    print(item)
    colour.write(item + '\n')

print(f'Total data of the file: {str(len(total))}')
