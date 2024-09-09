'''
1 <= N <= 4
2 <= W <= 12
2 <= H <= 15
'''
import sys

sys.stdin = open('sample_input (4).txt','r')
dr = [-1,1,0,0]  # 상하좌우 델타
dc = [0,0,-1,1]
def shoot(level, remains, now_arr):
    global min_b

    if level == N or remains == 0:
        min_b = min(min_b,remains)
        return
    '''
    1. col 위치에 쏘기 전 상태 복사
    2. 복사한 리스트의 clo 위치에 구슬 쏘기
    3. level + 1번 상태로 이동(다음 재귀 호출) + col 위치에 쏘고 난 상태도 전달
    '''
    for col in range(W):
        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬 쏘기
        # 1. 열 기준으로 가장 위에 있는 벽돌 찾기
        row = -1 # 벽돌이 없다고 가정
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break
        if row == -1: # 벽돌이 없는 열이면 다음 열로 넘어가기
            continue
        # 2. 연쇄적으로 깨질 벽돌
        # 행,열,벽돌 숫자
        stack = [(row,col, copy_arr[row][col])] # 앞으로 깨져야할 벽돌들 저장
        now_remains = remains - 1
        copy_arr[row][col] = 0

        while stack:
            r,c,p = stack.pop()
            for k in range(1,p):
                for i in range(4):
                    nr = r + (dr[i] * k)
                    nc = c + (dc[i] * k)
                    if 0 <= nr < H and 0 <= nc < W and copy_arr[nr][nc]:
                        stack.append((nr,nc,copy_arr[nr][nc])) # 다음 벽돌 추가
                        copy_arr[nr][nc] = 0 # 벽돌 깨짐
                        now_remains -= 1
        # 벽돌을 깬 후 빈칸 메꾸기
        for c in range(W):
            idx = H - 1 # 벽돌이 위치할 index
            for r in range(H-1,-1,-1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c] , copy_arr[r][c]
                    idx -= 1
        shoot(level+1, now_remains, copy_arr)

T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(H)]

    min_b = 1e9
    blocks = 0
    for i in range(H):
        for j in range(W):
            if array[i][j]:
                blocks += 1
    shoot(0,blocks,array)
    print(min_b)
