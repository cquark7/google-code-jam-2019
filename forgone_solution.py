# Main idea is that 4 can be represented as the sum of two digits:
# 4 = 1 + 3 = 2 + 2

for tc in range(int(input())):
    # take input as a string
    number = input()
    A = number
    B = ['0']*len(number)

    for idx, digit in enumerate(number):
        if digit == '4':
            B[idx] = '1'

    A = A.replace('4', '3')

    # remove leading zeroes
    B = ''.join(B).lstrip('0')

    print('Case #{}: {} {}'.format(tc+1, A, B))
