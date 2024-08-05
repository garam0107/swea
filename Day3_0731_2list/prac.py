N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

total = 0
for i in range(N):
    for j in range(N): # N*N 배열의 모든 원소
        s = 0 # 문제에서 원소와 인접한 원소간의 차의 절댓값의 합
        for k in range(4): # 원소의 4방향
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                s += abs(arr[i][j] - arr[ni][nj])
        total += s
print(total)
