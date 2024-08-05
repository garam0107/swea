import sys
sys.stdin = open('input.txt', 'r')

T = 10

for _ in range(1, T+1):
    N = 100
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col =0
    for idx in range(N):
        if arr[99][idx] == 2:
            col = idx
            break
    dr = [0,0,-1]
    dc = [-1,1,0]

    row = N - 1
    while row > 0:
        for i in range(3):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    arr[row][col] = 0
                    row = nr
                    col = nc

    print(f'#{tc} {col}')

