import math

s = int(input().strip())
sum = 0
n = 0

while sum + (n + 1) <= s :
    n += 1
    sum += n

print(n)