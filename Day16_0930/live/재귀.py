def rec(x):
    if x == 6:
        return
    print(x, end=' ')
    rec(x+1)
    print(x, end=' ')


def kfc(x):
    if x == 3:
        return
    for _ in range(4):
        kfc(x+1)
kfc(0)
