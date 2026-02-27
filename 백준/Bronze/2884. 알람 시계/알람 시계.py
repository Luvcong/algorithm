hour, minit = map(int, input().split())

total = (hour * 60) + minit
total -= 45

if total < 0 :
    total += 24 * 60
    
print(total // 60, total % 60)