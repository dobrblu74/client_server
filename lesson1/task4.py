list = ['разработка', 'администрирование', 'protocol', 'standard']
for i in list:
    a = i.encode('utf-8')
    print(f'Тип переменной:{type(a)}'
          f'Содержимое переменной:{a}')
    b = bytes.decode(a, 'utf-8')
    print(f'Тип переменной:{type(b)}'
          f'Содержимое переменной:{b}')



