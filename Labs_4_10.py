#1
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
def refer(point):
    return sum(point) / len(point)
print(min(numbers, key=refer))
print(max(numbers, key=refer))

#2
def map(function, items):
    result = []
    for item in items:
        result.append(function(round(item, 2)))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

print(*map(float, numbers), sep='\n')

#3
from cProfile import label
from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

print('Cities:', reduce(lambda a, b: f'{a}, {b}',list(sorted(map(lambda a: a[0], filter(lambda x: x if x[1] > 10000000 and x[2] == 'primary' else False, data))))))

#4
func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False

#5
list_ip = [int(x) if x.isdigit() else 300 for x in input().split('.')]
print(all([True if 256 > x >= 0 else False for x in list_ip ]))