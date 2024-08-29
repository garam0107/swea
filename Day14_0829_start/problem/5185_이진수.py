def binary(N,ls):
    if N == 0:
        for _ in range(4):
            ls.append(0)
        return ls
    if N == 1:
        ls.append(1)
        for _ in range(3):
            ls.append(0)
        return ls
    a = N % 2
    b = N // 2
    ls.append(a)
    if b == 1:
        ls.append(1)
        while len(ls) != 4:
            ls.append(0)
        return ls
    binary(b, ls)

T = int(input())
for tc in range(1,T+1):
    N,arr = map(str, input().split())
    sixteen = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    result = []
    for i in arr:
        list = []
        for idx in range(16):
            if i == sixteen[idx]:
                num = idx
                binary(num, list)
                answer = list[::-1]
                for i in answer:
                    result.append(i)
                break
    print(f'#{tc}',end=' ')
    for i in result:
        print(i,end='')
    print()
