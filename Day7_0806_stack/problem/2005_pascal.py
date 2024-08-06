def pascal(N):
    if N <= 2:
        array =  [1] * N
    if N >= 3:
        new = []
        array = pascal(N-1)
        for i in range(N-2):
            new += [array[i]+array[i+1]]
        array = [1] + new + [1]
    return array


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(1,N+1):
        print(' '.join(map(str, pascal(i))))