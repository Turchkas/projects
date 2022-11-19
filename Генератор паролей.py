from random import sample, randint, choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation ='!#$%&*+-=?@^'

def generate_password(length, chars):
    chars = sample(chars, int(lenght))
    s = ''
    for c in chars:
        s += c
    return s

flag = True

while flag==True:

    chars = ''

    print('Длина одного пароля?')
    lenght = input()
    while lenght.isdecimal()==False or lenght=='0':
        print('Введи НАТУРАЛЬНОЕ ЧИСЛО')
        lenght = input()

    print('Вводи да/нет, yes/no, y/n в любом регистре')
    print()
    print('Включать ли цифры 0123456789?')
    s = input()
    while s.lower() not in ('no', 'нет', 'n', 'н'):
        if s.lower() in ('да', 'yes', 'y'):
            for i in range(int(lenght)):
                chars += choice(digits)
                s = 'no'
        else:
            print('Повтори?')
            s = input()

    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
    s = input()
    while s.lower() not in ('no', 'нет', 'n', 'н'):
        if s.lower() in ('да', 'yes', 'y'):
            for i in range(int(lenght)):
                chars += choice(uppercase_letters)
                s = 'no'
        else:
            print('Повтори?')
            s = input()

    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
    s = input()
    while s.lower() not in ('no', 'нет', 'n'):
        if s.lower() in ('да', 'yes', 'y'):
            for i in range(int(lenght)):
                chars += choice(lowercase_letters)
                s = 'no'
        else:
            print('Повтори?')
            s = input()

    print('Включать ли символы !#$%&*+-=?@^_?')
    s = input()
    while s.lower() not in ('no', 'нет', 'n'):
        if s.lower() in ('да', 'yes', 'y'):
            for i in range(int(lenght)):
                chars += choice(punctuation)
                s = 'no'
        else:
            print('Повтори?')
            s = input()

    print('Исключать ли неоднозначные символы il1Lo0O?')
    s = input()
    while s.lower() not in ('no', 'нет', 'n'):
        if s.lower() in ('да', 'yes', 'y'):
            if len(chars) > 0:
                for c in chars:
                    if c in ('i', 'l', '1', 'L', 'o', '0', 'O'):
                        chars = chars.replace(c, '')
                        s = 'no'
            else:
                s = 'no'
        else:
            print('Повтори?')
            s = input()

    print('Количество паролей для генерации?')
    n = input()
    while n.isdecimal()==False or n=='0':
        print('Введи НАТУРАЛЬНОЕ ЧИСЛО')
        n = input()
    if len(chars)==0:
        print('Дурак что ли, я из чего составлять должен?')
    else:
        for i in range(int(n)):
            print(generate_password(int(lenght), chars))

    print('Закончим на этом?')
    s = input() 
    while s.lower() not in ('no', 'нет', 'n'):
        if s.lower() in ('да', 'yes', 'y'):
            flag = False
            break
        else:
            print('Повтори?')
            s = input()

