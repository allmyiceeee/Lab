#1
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []
sotka = (100,)
for i in range(len(tuples)):
    tuples[i] += sotka
    new_tuples.append(tuples[i][:-2] + sotka)
print(new_tuples)
#2
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = []
for i in range(len(tuples)):
    if len(tuples[i]) > 0:
        non_empty_tuples.append(tuples[i])


print(non_empty_tuples)
#3
a, b, c = int(input()), int(input()), int(input())
top = ((-b/(2 * a)),  (4 * a * c - b ** 2) / (4 * a))
print(top)
#4
a = int(input())
l = []
for i in range(a):
    l.append(input().split())
for _ in range(a):
    print(*l[_])
print()
for c in range(a):
    if int(l[c][1]) > 3:
        print(*l[c])
#5
n = int(input())
tuple1 = [1, 1, 1]
for i in range(3, n):
    tuple1.append(tuple1[i-1] + tuple1[i - 2] + tuple1[i - 3])
print(*tuple1[:n])

