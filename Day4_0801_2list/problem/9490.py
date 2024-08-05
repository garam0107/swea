T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    maxValue = 0
    for i in range(N):
        for j in range(M):
            flower = arr[i][j]
            sum = flower
            for a in range(1, flower + 1):
                for k in range(4):
                    ni = i + di[k]*a
                    nj = j + dj[k]*a
                    if 0 <= ni < N and 0 <= nj < M:
                        sum += arr[ni][nj]
                    if maxValue < sum:
                        maxValue = sum

    print(maxValue)





