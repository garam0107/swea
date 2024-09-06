
def square():
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0<= nr < N and 0 <= nc < N:
                    if array[i][j] + 1 == array[nr][nc]:
                        seq_list[array[i][j]] = 1
                        break




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    seq_list = [0] * (N*N+1)
    square()
    max = 0
    cnt = 1
    s_idx = 0
    for i in range(N*N,-1,-1): # 앞에서부터 탐색을 하면 마지막 방의 인덱스가 출력 되기 때문에 뒤에서 부터 탐색
        if seq_list[i] == 1:
            cnt += 1
        else:
            if max <= cnt:
                max = cnt
                s_idx = i+1
            cnt = 1
    print(f'#{tc} {s_idx} {max}')

