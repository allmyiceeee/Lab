#1
if int(input()) % 100 == 00:
    print('Yes')
else:
    print('No')
#2
a1 , b1 , a2 , b2 = int(input()) , int(input()) , int(input()) , int(input())
if (a1 + b1 + a2 + b2) % 2 == 0:
    print('YES')
else:
    print('NO')
#3
age , pol = int(input()) , input()
if 10 <= age <= 15 and pol == 'f':
    print('YES')
else:
    print('NO')
#4
romam_numerals = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X'}
numerals = int(input())
if numerals in romam_numerals:
    print(romam_numerals[numerals])
else:
    print('Ошибка')
#5-6?
a1 , b1 , a2 , b2 = int(input()) , int(input()) , int(input()) , int(input())
if a1 + b1 == a2 + b2 or a1 - b1 == a2 - b2:
    print('YES')
else:
    print('NO')
#7
x1 , y1 , x2 , y2 = int(input()) , int(input()) , int(input()) , int(input())
a = x1 - x2
b = y1 - y2
if a * b == 2 or a * b == -2:
    print('YES')
else:
    print('NO')
#8
x1 , y1 , x2 , y2 = int(input()) , int(input()) , int(input()) , int(input())
if x1 == x2 or y1 == y2:
    print('YES')
elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
    print('YES')
else:
    print("NO")
