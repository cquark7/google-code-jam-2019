for _ in range(1, int(input()) + 1):
    input()
    ans = ''
    for i in input().strip():
        if i == 'S':
            ans += 'E'
        else:
            ans += 'S'
    print('Case #{0}: {1}'.format(_, ans))
