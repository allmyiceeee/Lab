#1
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
print(*sorted(fruits, reverse = True), sep = '\n')
#2
my_set = set(input() + input())
if len(my_set) == 10:
    print("YES")
else:
     print("NO")
#3
n = int(input())
for i in range(n):
    print(len(set(input().lower())))
#4
n = int(input())
str = ''
for i in range(n):
    str += input().lower()
print(len(set(str)))
#5
strok = input().lower().split()
strok2 = []
for i in range(len(strok)):
    strok2.append(strok[i].strip(".,;:-?!"))
print(len(set(strok2)))
#6
lst = list(map(int, input().split()))
my_set = set()
for i in range(len(lst)):
    if lst[i] in my_set:
        print("YES")

    else:
        print("NO")
        my_set.add(lst[i])

