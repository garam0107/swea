def graph(node):
    if node == 0:
        return
    preorder.append(node)
    graph(adjl[node][0])
    graph(adjl[node][1])



T = int(input())
for tc in range(1,T+1):
    E,N = map(int, input().split())
    array = list(map(int, input().split()))
    adjl = [[] for _ in range((max(array)+1))]
    for i in range(E):
        parent,child = array[i*2],array[i*2+1]
        adjl[parent].append(child)

    for i in range(len(adjl)):
        while len(adjl[i]) < 2:
            adjl[i].append(0)
    preorder = []
    graph(N)
    answer = len(preorder)
    print(f'#{tc} {answer}')
