from random import *

print('Добро пожаловать в числовую угадайку')

def is_max_number():
    while True:
        n = input('Введите максимальное число которое мы можем загадать: ')
        if n.isdigit():
            return int(n)
        else:
            print('Попробуйте еще раз. Необходимо ввести именно число, а не текст')

max_number = is_max_number()

def is_valid(number):
    return number.isdigit() and 1 <= int(number) <= max_number


def input_num():
    while True:
        n = input(f'Введите число от 1 до {max_number}: ', )
        if is_valid(n):
            return int(n)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {max_number}?')


def compare_numbers():
    counter = 1
    rand = randint(1, max_number)
    while True:
        result = input_num()
        if result < rand:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        elif result > rand:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        else:
            print(f'Вы угадали, поздравляем!')
            print(f'Кол-во потраченных попыток: {counter}')
            break


compare_numbers()
while True:
    print('Хотите сыграть еще раз? (Да/Нет)')
    answer = input()
    if answer.lower() == 'да' or answer.lower() == "д" or answer.lower() == 'yes':
        max_number = int(input('Введите максимальное число которое мы можем загадать: ', ))
        compare_numbers()
    elif answer.lower() == 'нет' or answer.lower() == "н" or answer.lower() == 'no':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        print('Я вас не понял, так вы хотите поиграть?')

