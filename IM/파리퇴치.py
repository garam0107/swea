def bug(array,N,M):
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for r in range(M):
                for c in range(M):
                    sum += array[i+r][j+c]
            if max_v < sum:
                max_v = sum
    return max_v
T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    answer = bug(array,N,M)
    print(answer)