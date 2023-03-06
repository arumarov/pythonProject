# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
a = 10
for i in range(a):
    attempt = int(input('Введите число: '))
    if attempt == num:
        print('Йохххууу!!! Вы выиграли кучу денег!!!')
        quit()
    else:
        if attempt < num:
            print('Попробуйте число побольше')
            print('У вас осталось', a - i - 1, 'попыток')
        else:
            print('Попробуйте число поменьше')
            print('У вас осталось', a - i - 1, 'попыток')
print('Игра закончена, у вас закончились попытки!')