from math import gcd


def decode(cip: list):
    for i in range(L - 1):
        if cip[i] != cip[i + 1]: 
            break

    ans = [0] * (L + 1)
    c = gcd(cip[i], cip[i + 1])
    ans[i + 1] = c
    for j in range(i + 2, len(ans)):
        ans[j] = cip[j - 1] // ans[j - 1]
    for j in range(i, -1, -1):
        ans[j] = cip[j] // ans[j + 1]

    primes = sorted(set(ans))
    inv = {p: i for i, p in enumerate(primes)}
    return ''.join(chr(ord('A') + inv[i]) for i in ans)


for tc in range(int(input())):
    N, L = map(int, input().split())
    cipher = list(map(int, input().split()))
    anagram = decode(cipher)
    print("Case #{}: {}".format(tc+1, anagram))
