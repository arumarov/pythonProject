# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

a = int(input("Введите число: "))
print(hex(a))
b = 16
num = 1
num1 = 1
result = ''
while num > 0:
    num = a//b
    num1 = a%b
    a = num
    if num1 == 10:
        result = 'a' + result
    elif num1 == 11:
        result = 'b' + result
    elif num1 == 12:
        result = 'c' + result
    elif num1 == 13:
        result = 'd' + result
    elif num1 == 14:
        result = 'e' + result
    elif num1 == 15:
        result = 'f' + result
    else:
        result = str(num1) + result
result = '0x' + result
print(result)