# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

if a<=b+c or b<=a+c or c<=a+b:
    if a == b and b == c:
        print ('Треугольник является равносторонним')
    elif a == b or a == c or b == c:
        print('Треугольник является равнобедренным')
    else:
        print('Треугольник является разносторонним')
else:
    print('Треугольника с такими сторонами не существует')