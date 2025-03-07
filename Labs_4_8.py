#1
print(len(set(input().split()).intersection(set(input().split()))))
#2
i1 = set(input().split())
i2 = set(input().split())
lst = list(map(int, i1.intersection(i2)))
print(*sorted(lst))
#3
if set(map(int, input())).isdisjoint(set(map(int, input()))):
    print("NO")
else:
    print("YES")
#4
if set(map(int, input())).issuperset(set(map(int, input()))):
    print("YES")
else:
    print("NO")

#5
mark1 = set(map(int, input().split()))
mark2 = set(map(int, input().split()))
mark3 = set(map(int, input().split()))

mark1.intersection_update(mark2)

print(*sorted(mark1.difference(mark3), reverse= True))
#6
files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

file = {i.lower() for i in files if i.lower().endswith('png')}
print(*sorted(file))
