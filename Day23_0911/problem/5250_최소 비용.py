# 다익스트라로 풀기
from collections import deque



dr = [0,1]
dc = [1,0]
T = int(input())


def dijkstra(r,c):
    global ans




    pass


for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    ans = 1e9
    dp = [[1e9]*N for _ in range(N)] # 가중치 저장하는 리스트
    dijkstra(0,0)




