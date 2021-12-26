import locale
list_string = ['сетевое программирование', 'сокет', 'декоратор']

with open('test.txt', 'w+') as f_n:
    for i in list_string:
        f_n.write(i + '\n')
        print(f_n)

file_coding = locale.getpreferredencoding()
print(file_coding)

with open('test.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')

