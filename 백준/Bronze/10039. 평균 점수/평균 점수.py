import sys

score = list(map(int, sys.stdin.read().split()))
total = 0

for s in score :
    total += max(s, 40)

print(int(total/len(score)))