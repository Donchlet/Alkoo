import re


my_text = 'Vlad, 1997, vlad@gmail.com, $4000, male* ' \
          'John, 1980, john@yahoo.com, $500, male* ' \
          'Max, 1999, max@yandex.ru, $200, female& ' \
          'Fred, 1995, fred@mail.ru, $800, female& ' \


"""
\d -- Он ищет подряд стоящие ЧИСЛА [0-9]
\В -- Он ищет любые, но не числа
\w -- Ищет любой алфавитный символ [A-Z a-z]
\s -- Ищет пробелы
\S -- Специальные символы
"""



file_path = 'demo_mock_data.txt'
result_file_path = 'results.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()

what_search = r'@\w+,\w.[a-z]+'
results = re.findall(what_search, my_text_file)

for i in results:
    print(i)
    result_file.write(i)

print(f'Total: {str(len(results))}')









