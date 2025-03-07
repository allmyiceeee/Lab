#1
for i in range(10):
    print('Python is awesome!')
#2
text , kolvo = input() , int(input())
for i in range(kolvo):
    print(text)
#3
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')
#4
a = int(input())
for i in range(a):
    print("*" * 19)
#5
a = input()
for i in range(10):
    print(i , a)
#6
n = int(input())
for i in range(n+1):
    print('Квадрат числа' , i , 'равен', i**2)
#7
k=int(input())
for i in range(k):
    print((k-i)* '*')
#8
m,n,p = int(input()) , int(input()), int(input())
for i  in range(p):
    a =m* (n/100 + 1)**i
    print(i + 1, a)


