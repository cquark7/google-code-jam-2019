for tc in range(int(input())):
    N = int(input())
    lydia_path = input()
    # I am such an original thinker, LoL
    my_path = ''.join('E' if p == 'S' else 'S' for p in lydia_path)
    print('Case #{}: {}'.format(tc + 1, my_path))
