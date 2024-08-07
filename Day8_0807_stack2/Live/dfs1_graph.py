def dfs_graph(s, V):
    visit = [0]*(V+1)
    graph_stack = []
    print(s)
    visit[s] = 1
    v = s # 현재 정점
    while True:
        for w in adjl[v]:
            if visit[w] == 0:
                graph_stack.append(v)
                v = w
                print(v)# w에 방문
                visit[w] = 1   # w에 방문 표시
                break # for문 종료
        else: # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if graph_stack:
                v = graph_stack.pop()
            else:  # 되돌아갈 곳이 없으면 남은 갈림길이 없는 거니까 탐색 종료
                break # while True 종료






# 인접 리스트 만들기
# 인접 리스트[0]은 None
# 인접 리스트의 [1]은 1에 인접인 정점
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2] , arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)
    print(adjl)
    # dfs_graph(1,V)