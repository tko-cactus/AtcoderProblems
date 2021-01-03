from itertools import product

count = 0

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]

sum1 = [[b[line - 1] * a[row - 1][line - 1]
         for line in range(m)] for row in range(n)]

sum = [sum(i) for i in sum1]

for i in sum:
    if i + c > 0:
        count += 1

print(count)
