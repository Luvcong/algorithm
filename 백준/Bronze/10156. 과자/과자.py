k, n, m = map(int, input().split())
total = k * n
print(max((total - m), 0))