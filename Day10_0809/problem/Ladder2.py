def ladder_2(array,N):
    col_list=[]
    for i in range(N):
        if array[0][i] == 1:
            col_list.append(i)

    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    min_v = 100
    min_col = 0
    row = 0
    visit = [[0]*N for _ in range(N)]
    for col in col_list:
        counts = 0
        while row < N-1:
            for k in range(3):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0:
                    if array[nr][nc] == 1:
                        counts += 1
                        row = nr
                        col = nc
                        break
        if min_v > counts:
            min_v = counts

    return min_v

import sys
sys.stdin = open('input.txt', 'r')


T = 10
for _ in range(1,T+1):
    tc = int(input())
    N = 100
    array = [list(map(int, input().split())) for _ in range(N)]
    print(ladder_2(array,N))





