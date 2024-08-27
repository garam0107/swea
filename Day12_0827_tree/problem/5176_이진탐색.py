def make_order(node):  # 중위 순회
    if node == 0:
        return
    make_order(order[node][0])
    order_list.append(node)
    make_order(order[node][1])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1) #트리의 노드 번호 마다 값을 저장할 리스트
    order = [[] for _ in range(N+1)] #인접 리스트 만들기 위함
    number = 1
    for i in range(1,N+1):
        left = i*2
        right = i*2 + 1
        if left <= N:            #자식 노드가 N 보다 크면 저장할 필요 없음
            order[i].append(left)
        if right <= N:
            order[i].append(right)
    for i in range(N+1):         # 인덱스 에러 방지하기 위해 자식 노드가 없을 때 0을 넣어줌줌
        while len(order[i]) < 2:
            order[i].append(0)
    order_list = []    # 중위 순회할 때 순서 저장
    make_order(1)
    # 맨 첫번째 순서에 1을 저장하고 그 다음부터 1을 추가해서 중위 순회 순서대로 tree에 넣어줌
    for i in order_list:
        tree[i] = number
        number += 1

    print(f'#{tc} {tree[1]} {tree[N//2]}')





