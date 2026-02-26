idx = int(input().strip())

total = []
for _ in range(idx) :
    x, y, z = sorted(map(int, input().split()))
    if x == y == z :
        total.append(10000 + x * 1000)
    elif x == y or y == z :
        total.append(1000 + y * 100)
    else :
        total.append(max(x, y, z) * 100)
print(max(total))