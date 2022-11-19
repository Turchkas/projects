ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lower = 'abcdefghijklmnopqrstuvwxyz'

flag = True

print('Зашифруй свой текст\n')

def encrypt(s, language, n, k):
    if n==1:
        if language=='ru':
            list = ''
            for c in s:
                x1 = ru_lower.find(c)
                x2 = ru_upper.find(c)
                if x1==-1 and x2==-1:
                    list += c
                elif x1!=-1 and x2==-1:
                    y = (x1 + k)%32
                    c = ru_lower[y]
                    list += c
                elif x1==-1 and x2!=-1:
                    y = (x2 + k)%32
                    c = ru_upper[y]
                    list += c
            print(list)
        elif language=='en':
            list = ''
            for c in s:
                x1 = en_lower.find(c)
                x2 = en_upper.find(c)
                if x1==-1 and x2==-1:
                    list += c
                elif x1!=-1 and x2==-1:
                    y = (x1 + k)%26
                    c = en_lower[y]
                    list += c
                elif x1==-1 and x2!=-1:
                    y = (x2 + k)%26
                    c = en_upper[y]
                    list += c
            print(list)
    elif n==2:
        if language=='ru':
            list = ''
            for c in s:
                x1 = ru_lower.find(c)
                x2 = ru_upper.find(c)
                if x1==-1 and x2==-1:
                    list += c
                elif x1!=-1 and x2==-1:
                    y = (x1 - k)%32
                    c = ru_lower[y]
                    list += c
                elif x1==-1 and x2!=-1:
                    y = (x2 - k)%32
                    c = ru_upper[y]
                    list += c
            print(list)
        elif language=='en':
            list = ''
            for c in s:
                x1 = en_lower.find(c)
                x2 = en_upper.find(c)
                if x1==-1 and x2==-1:
                    list += c
                elif x1!=-1 and x2==-1:
                    y = (x1 - k)%26
                    c = en_lower[y]
                    list += c
                elif x1==-1 and x2!=-1:
                    y = (x2 - k)%26
                    c = en_upper[y]
                    list += c
            print(list)

while flag==True:
    print('Выбери язык сообщения: ru или en')
    language = input()
    while language not in ('ru', 'en'):
        print('Повтори?')
        language = input()
    
    print('Выберите 1, если зашифровать, и 2, если дешифровать')
    n = input()
    while n not in ('1', '2'):
        print('Повтори?')
        n = input()
    n = int(n)

    print('Введите шаг сдвига')
    k = input()
    while k.isdigit()==False:
        print('Повтори?')
        k = input()
    k = int(k)

    if language=='ru':
        print('Вводи только буквы русского алфавита, иные символы не подвергнутся шифровке')
    elif language=='en':
        print('Вводи только буквы английского алфавита, иные символы не подвергнутся шифровке')
    s = input()

    encrypt(s, language, n, k)

    print()

    print('Закончим на этом?')
    s = input() 
    while s.lower() not in ('no', 'нет', 'n'):
        if s.lower() in ('да', 'yes', 'y'):
            flag = False
            break
        else:
            print('Повтори?')
            s = input()