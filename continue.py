from random import randint
a = randint(1, 10)
b = randint(1, 10)
result = a + b
answer = int(input('Сколько будет %(a)i + %(b)i = ' % {
        'a': a, 'b': b }))
while True:
    result = a + b
    answer = int(input('Сколько будет %(a)i + %(b)i = ' % {
        'a': a, 'b': b }))
    if answer != result:
        print('Нет, попробуй ещё раз ')
        continue
    print('Верно')
    a = randint(1, 10)
    b = randint(1, 10)