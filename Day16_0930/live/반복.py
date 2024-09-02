def bts(x):
    x += 10
    print(x)


def kfc(x):
    print(x)
    x += 3
    bts(x+2)
    print(x)

x = 3
kfc(x+1)
print(x)
