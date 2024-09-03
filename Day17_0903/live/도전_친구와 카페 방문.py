arr = ['a','b','c','d','e']
n = len(arr)
def get_sub(tar):
    cnt= 0
    for i in range(n):
        if tar & 1:
            cnt += 1
        tar >>= 1
    return cnt


result = 0
for tar in range(0,2**n):
    if get_sub(tar) >= 2:
        result += 1
print(result)