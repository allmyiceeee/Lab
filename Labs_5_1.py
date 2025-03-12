#1
files = input()
file_1 = open(files, 'r')

for line in file_1:
    print(line.strip())

file_1.close()

#2

files = input()
file_1 = open(files, 'r')
file2 = file_1.readlines()
print(file2[-2])

file_1.close()

#3
file = open('prices.txt', 'r', encoding= 'utf-8')
counter = 0
for line in file:
    line_1 = line.split()
    counter += int(line_1[1]) * int(line_1[2])
file.close()
print(counter)

#4
file_country = open('population.txt', 'r')
for line in file_country:
    line = line.split()
    if line[0][0] == 'G' and int(line[-1]) > 500000:
        print(line[0])
file_country.close()

#5
def read_csv():
    with open('data.csv', 'r') as file:
        keys = file.readline().rstrip().split(',')
        arr_val = [x.strip().split(',') for x in file.readlines()]
        list_final = [dict(zip(keys, values)) for values in arr_val]
        return list_final
print(read_csv())