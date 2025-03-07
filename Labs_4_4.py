#1
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
#2
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0
for i in range(len(list1)):
    if max(list1[i]) > maximum:
        maximum = max(list1[i])
print(maximum)
#3
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in range(len(list1)):
    total += sum(list1[i])
    counter += len(list1[i])
print(total/counter)
#4
n = int(input())
list = []
for i in range(1, n + 1):
    list.append(i)
for i in range(1, n + 1):
    print(list)
#5
n = int(input())
for x in range(1, n + 1):
    for i in range(1, x + 1):
        my_list = list(range(1, x + 1))
    print(my_list)
#6
stroka = input()
list3 = []
a = []
for i in stroka.split():
    if not a:
        a.append(i)
    else:
        if i == a[-1]:
            a.append(i)
        else:
            list3.append(a)
            a = []
            a.append(i)

if a:
    list3.append(a)
print(list3)
