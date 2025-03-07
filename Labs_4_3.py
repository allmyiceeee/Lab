#1
line = input().split()
print(*line , sep = '\n')
#2
line = input().split('\\')
print(*line , sep = '\n')
#3
line = input().split('.')
for i in line:
    if 0 > int(i) or int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')
#4
a = input()
lst = a.split()
counter = 0
for i in range(len(lst) - 1):
    for _ in range(i + 1 , len(lst)):
        if lst[i] == lst[_]:
            counter += 1
print(counter)
#5
list = input().split()
for i in range(len(list)):
    list[i] = int(list[i])
if len(list) == 1:
    print(*list)
else:
    findmax = max(list)
    findmin = min(list)
    indexmax = list.index(findmax)
    indexmin = list.index(findmin)
    list.remove(findmin)
    list.remove(findmax)
    list.insert(indexmin,findmax)
    list.insert(indexmax, findmin)
    print(*list)
#7
for i in range(100, 1001):
    if str(i) == str(i)[::-1]:
        print(i)