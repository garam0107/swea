T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    num_list = []
    for i in range(N):
        for j in range(M):