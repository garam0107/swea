arr = ['a','b','c']
n = len(arr)
def get_sub(tar):
    for i in range(n):
        if tar & 0x1: # tar변수와 1을 & 연산으로 0과 1 체크
            print(arr[i], end=' ')
        tar >>= 1

for tar in range(0, 2**3):
    print('{',end=' ')
    get_sub(tar)
    print('}')