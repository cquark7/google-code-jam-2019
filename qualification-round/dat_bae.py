store = [''.join(bin(x % 32)[2:].zfill(6)[5 - i] for x in range(1024))
              for i in range(5)]


for t in range(int(input())):
    n, b, f = map(int, input().split())
    responses = []
    for q in range(5):
        print(store[q][:n], flush=True)
        responses.append(input())
    bad_machines = []
    good_machines = [int(''.join(reversed(num)), 2)
                     for num in zip(*responses)]
    gidx = 0
    for i in range(n):
        if gidx >= len(good_machines) or i % 32 != good_machines[gidx]:
            bad_machines.append(i)
        else:
            gidx += 1

    print(*bad_machines, flush=True)
    input()
