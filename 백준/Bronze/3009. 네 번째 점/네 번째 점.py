xor_x = xor_y = 0
for _ in range(3) :
    x, y = map(int, input().split())
    xor_x ^= x
    xor_y ^= y
print(xor_x, xor_y)

# x_list = []
# y_list = []

# for _ in range(3) :
#     x, y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)

# x = next(x for x in x_list if x_list.count(x) == 1)
# y = next(y for y in y_list if y_list.count(y) == 1)
# print(x, y)

'''
직사각형의 경우 x, y 좌표가 각각 2개씩 존재 
=> 각각 리스트를 만들어서 1개만 있는 값이 어떤 값인지 확인하여 출력 (count)
=> XOR 방식을 이용하여 값 출력
    - 항등원 : 0과 연산하면 자기 자신이 출력 (5 ^ 0 = 5)
    - 역원   : 같은 수끼리 연산하면 0 출력   (5 ^ 5 = 0)
    - 교환/결합법칙 : 연산 순서에 상관없이 결과 동일
'''