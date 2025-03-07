#1
n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for c in range(m):
        matrix[i][c] = (input())
for i in range(0, n):
    print(*matrix[i])
#2
n, m = int(input()), int(input())
matrix = [[0] * m for _ in range(n)]
for i in range(n):
    for c in range(m):
        matrix[i][c] = (input())
for i in range(0, n):
    print(*matrix[i])
print()
for c in range(0, m):
    for r in range(0, n):
        print(matrix[r][c], end=' ')
    print()
#3
cols = int(input())
counter = 0
matrix = [[0] * cols for _ in range(cols)]
for i in range(cols):
    matrix[i] = input().split()
for i in range(cols):
    counter += int(matrix[i][i])


print(counter)
#4
cols = int(input())
matrix = [list(map(int, input().split())) for _ in range(cols)]
maximum = -1000
for i in range(cols):
    for j in range(cols):
        if i > j and i < cols - 1 - j or i > j and i > cols - 1 - j or i >= j:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)
#5
rows, cols = int(input()), int(input())
matrix = [[0] * cols for _ in range(rows)]
for r in range(rows):
    for c in range(cols):
        matrix[r][c] = str(r * c).ljust(3)
for _ in range(rows):
    print(*matrix[_])
#6
cols = int(input())
matrix = [list(map(int, input().split())) for _ in range(cols)]
maximum = -1000
for i in range(cols):
    for j in range(cols):
        if i > j and i < cols - 1 - j or i == j or i < j and i > cols - 1 - j or j == cols - 1 - i:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)