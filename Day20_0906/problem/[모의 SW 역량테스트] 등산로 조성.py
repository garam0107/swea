import sys
sys.stdin = open('sample_input.txt','r')
# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def max_index():
    for i in range(N):
        for j in range(N):
            if mou[i][j] == max_h:
                max_idx_list.append((i,j))
def dfs(row,col):





T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    mou = [list(map(int,input().split())) for _ in range(N)]
    max_h = 0
    max_idx_list = []
    k_list = []
    for i in range(1,K+1):
        k_list.append(i)
    for i in range(N):
        h = max(mou[i])
        if max_h <= h:
            max_h = h
    max_index()
    for r,c in max_idx_list:
        dfs(r,c)


