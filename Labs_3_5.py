#1
x1 , y1 , x2 , y2 = float(input()) , float(input()) , float(input()) ,float (input())
import math as m
a = m.sqrt(pow((x1 - x2) , 2) + pow((y1 - y2) , 2))
print(a)
#2
R = float(input())
import math as m
S = m.pi * pow(R , 2)
C = 2 * m.pi * R
print(S)
print(C)
#3
a , b = float(input()) , float(input())
import math as m
print((a + b) / 2)
print(m.sqrt(a * b))
print((2 * a * b) / (a + b))
print(m.sqrt((m.pow(a , 2) + m.pow(b , 2)) / 2))
#4
r = float(input())
import math as m
a = m.radians(r)
y = m.sin(a) + m.cos(a) + m.pow(m.tan(a) , 2)
print(y)
#5
a = float(input())
import math as m
print(m.ceil(a) + m.floor(a))
#6
a , b , c = float(input()) , float(input()) , float(input())
D = b ** 2 - 4 * a * c
if D == 0:
    print(-b / (2 * a))
elif D >= 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print(min(x1 , x2))
    print(max(x1 , x2))
else:
    print('Нет корней')
#7
n , a = float(input()) , float(input())
import math as m
print((n * a ** 2) / (4 * m.tan(m.pi / n)))