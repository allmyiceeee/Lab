#1
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
user = []
for i in range(len(users)):
    if users[i]['phone'][-1] == '8':
        user.append(users[i]['name'])
print(*sorted(user))
#2
courses = {'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'},
'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'},
'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}}
n = input()
print(f"{n}: {courses[n]['audience_number']}, {courses[n]['teacher']}, {courses[n]['time']}")
#3
morze = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}
n = input().upper()
list = []
for i in range(len(n)):
    if n[i] in morze:
        list.append(morze[n[i]])
print(*list)
#4
result = {}
for num in range(1, 16):
    result[num] = result.get(num, num) ** 2
#5
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}
result.update(dict1)
result.update(dict2)
for num in dict1:
    if num in dict1 and num in dict2:
        result[num] = dict1[num] + dict2[num]
#6
slovar = {}
slovo = input()
for i in slovo:
    slovar[i] = slovar.get(i, 0) + 1
sss = {}
for i in range(int(input())):
    p, j = input().split(':')
    sss[p] = int(j)
for _ in slovo:
    for key_slovar in slovar:
        for key_sss in sss:
            if _ == key_slovar and  sss[key_sss] == slovar[key_slovar]:
               slovo = slovo.replace(_, key_sss)
print(slovo)
