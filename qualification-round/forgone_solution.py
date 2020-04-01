# 4 can be represented as the sum of two digits:
# 4 = 1 + 3 = 2 + 2

for _ in range(1, int(input()) + 1):
    number = input().strip()
    A = number
    B = ''.join('1' if d == '4' else '0' for d in number).lstrip('0')
    A = A.replace('4', '3')
    print('Case #{0}: {1} {2}'.format(_, A, B))
