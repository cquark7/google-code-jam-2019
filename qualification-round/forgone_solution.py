# 4 can be represented as the sum of two digits:
# 4 = 1 + 3 = 2 + 2

for case in range(1, int(input()) + 1):
    A = input().strip()
    B = ''
    for digit in A:
        if digit == '4':
            B += '1'
        else:
            B += '0'
    B = B.lstrip('0')
    A = A.replace('4', '3')
    print('Case #{0}: {1} {2}'.format(case, A, B))
