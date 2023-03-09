# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 4, 6, 2, 8, 10, 12, 6, 6, 18, 4]
new_list = []
temp = 0
i = 0
res = 0
while temp < len(my_list):
    if my_list.count(my_list[temp]) > 1:
        new_list.append(my_list[temp])
        i = int(my_list.count(my_list[temp]))
        res = my_list[temp]
        while i >= 1:
            my_list.remove(res)
            i -= 1
        temp += 1
    else:
        temp += 1
my_list = new_list
print(my_list)
