import math

count = int(input())

for _ in range(count) :
    a, b = map(int, input().split())
    lcm = a * b // math.gcd(a, b)
    print(lcm)