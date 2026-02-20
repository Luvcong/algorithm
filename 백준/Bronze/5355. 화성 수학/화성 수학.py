count = int(input())
n = 0

for _ in range(count) :
    num, *args = input().split()
    num = float(num)

    for a in args :
        if a == '@' :
            num *= 3
        elif a == '%' :
            num += 5
        elif a == '#' :
            num -= 7
    
    print(f'{num:.2f}')