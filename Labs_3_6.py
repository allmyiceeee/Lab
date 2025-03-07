#1
a = input()
print('Футбольная команда' , a , 'имеет длину' , len(a) , 'символов')
#2
city = {}
for i in range(3):
    n = input()
    city[n] = len(n)
for k, v in city.items():
    if v == max(city.values()):
        print(k)
    if v == min(city.values()):
        print(k)
#3
a = input()
if '@' in a and '.' in a:
    print('YES')
else:
    print('NO')
#4
str = input()
for i in range(len(str)):
    if i % 2 == 0:
        print(str[i])
#5
print(input()[::-1])
#6
str = input()
print(f'Символ + встречается {str.count('+')} раз')
print(f'Символ + встречается {str.count('*')} раз')
#7
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
counter_vowels = 0
counter_consonants = 0
for i in input().lower():
    if i in vowels:
        counter_vowels += 1
    if i in consonants:
        counter_consonants += 1
print(f'Количество гласных букв равно {counter_vowels}')
print(f'Количество cогласных букв равно {counter_consonants}')


