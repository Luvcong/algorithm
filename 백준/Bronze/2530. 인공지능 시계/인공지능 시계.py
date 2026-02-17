a, b, c = map(int, input().split())
d = int(input())

total = (a * 3600) + (b * 60) + c + d

print((total // 3600) % 24, (total // 60) % 60, total % 60)