#Задание 1
print(int(input()) * int(input()) * int(input()) - 1)
#Задание 2
print(int(input()) // 100)
#Задание 3
n, k = int(input()), int(input())
print(f'Каждому достанется {k // n} мандаринов, останется {k % n}')
#Задание 4
n_v = int(input())
if n_v % 2 != 0:
    print(n_v // 2 + 1)
else:
    print(n_v // 2)
#Задание 5
print(int(input()) // 4 + 1)
#Задание 6
min = int(input())
print(f'Час - {min // 60} Минута - {min % 60}')
#Задание 7
test = input()
print(f'Сумма цифр = {int(test[0]) + int(test[1]) + int(test[2])}. Произведение = {int(test[0]) * int(test[1]) * int(test[2])}')
#Задание 8
abc = input()
a = abc[0]
b = abc[1]
c = abc[2]
print(f'{a + b + c}, {a + c + b}, {b + a + c}, {b + c + a}, {c + a + b}, {c + b + a}')
#Задание 9
count1 = int(input())
print(f' Цифра в позиции тысяч равна {count1 // 1000} \n Цифра в позиции сотен равна {(count1 //100) % 10} \n Цифра в позиции десятков равна {(count1 //10) % 10} \n Цифра в позиции единиц равна {count1 % 10}')