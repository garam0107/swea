
T = int(input())
for tc in range(1, T+1):
    def myMax(lst):
        maxNum = lst[0]
        for i in range(1, len(lst)):
            if maxNum > lst[i]:
                maxNum = maxNum
            else:
                maxNum = lst[i]
        return maxNum


    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N, M = map(int, (input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    totalList = [0] * N * M
    T = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
            totalList.append(s)


    print(f'#{tc} {myMax(totalList)}')
