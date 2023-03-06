# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

a = str(input("Введите дробь №1: "))
b = str(input("Введите дробь №2: "))
a_string = a.split("/")
b_string = b.split("/")
num1 = (int(a_string[0])) / (int(a_string[1]))
num2 = (int(b_string[0])) / (int(b_string[1]))

print('Сумма дробей: ', num1 + num2)
print('Произведение дробей: ', num1 * num2)

f1 = Fraction((int(a_string[0])), (int(a_string[1])))
f2 = Fraction((int(b_string[0])), (int(b_string[1])))
print('Сумма дробей: ', f1 + f2)
print('Произведение дробей: ', f1 * f2)
