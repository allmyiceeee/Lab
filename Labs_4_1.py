#1
s = input()
s1 = ''
for i in range(len(s)):
    if i % 3 != 0:
        s1 += s[i]
print(s1)
#2
s = input()
g = 0
for i in range(len(s)):
    g += int(s[i])
print(g)
#3
s = input()
counter = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        counter += 1
if counter > 0:
    print("Цифра")
else:
    print('Цифр нет')
#4
s = input()
counter = 0
if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
elif s.replace('f', 'g', 1):
    print(s.replace('f', 'g', 1).find('f'))
#5
s = input()
h1 = s.find('h')
h2 = s.rfind('h')
print(s[:h1] + s[h2:h1: -1] + s[h2:])
#6
counter = 0
s = input()
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        counter += 1
print(counter)
#7
des = int(input())
dv = str()
while des > 0:
    dv =  str(des % 2) + dv
    des //= 2
print(dv)
#8
n = int(input())
stroka = input()
stroka2 = ''
for i in stroka:
    if 96 > ord(i) - n:
        stroka2 += chr(ord(i) - n + 26)
    else:
        stroka2 += chr(ord(i) - n)
print(stroka2)