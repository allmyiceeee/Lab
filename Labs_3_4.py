#1
s , v1 , v2 = float(input()) , float(input()) , float(input())
print(s / (v1 + v2))
#2
a = float(input())
if a != 0:
    print(a ** -1)
else:
    print('Обратного числа не существует')
#3
a = int(input())
if a <= 2:
    print(a * 10.5)
elif a > 2:
    print(2 * 10.5 + (a - 2) * 4)
#4
a = float(input())
print(int((a * 10) % 10))
#5
a = float(input())
print(a - (a // 1))
#6
a , b , c = int(input()) , int(input()) , int(input())
print(max(a , b, c))
d = (a + b + c) - (max(a , b , c) + min(a , b , c))
print(d)

print(min(a , b , c))
#7
p1 , p2 , q1 , q2 = int(input()) , int(input()) , int(input()) , int(input())
rast = abs(p1 - q1) + abs(p2 - q2)
print(rast)