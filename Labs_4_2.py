#1
lst1 = []
for i in range(1, int(input()) + 1):
    lst1.append(i)
print(lst1)
#2
a = int(input())
s = []
for i in range(97 , a + 97 ):
    s +=chr(i)
print(s)
#3
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 and 17 in numbers:
    print("YES")
else:
    print("NO")
del numbers[0:1]
del numbers[-1:]
print(numbers)
#4
lst = []
n = int(input())
for i in range(n):
  lst.append(int(input()))
del lst[1::2]
print(lst)
#5
lst = []
lst2 = []
for i in range(int(input())):
    lst.append(input())

n = int(input())
for _ in range(0, len(lst)):
    if len(lst[_]) >= n:
        lst2.append(lst[_][n - 1])
print(*lst2 , sep = '')
#6
kolvo = int(input())
list = []
for i in range(kolvo):
    list.append(input())
zapros = input()
for i in range(kolvo):
    if zapros.lower() in list[i].lower():
        print(list[i])