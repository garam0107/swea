# tree에 삽입 후 부모 노드와 내 노드의 크기를 비교해 부모 노드의 값이 내 노드의 값보다 크다면 위치 교환
def enqueue(target): # 삽입을 위한 함수
    while target // 2:
        parent = target // 2
        if tree[target] <= tree[parent]:
            tree[target],tree[parent] = tree[parent],tree[target]
        target = parent

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0]
    array = list(map(int, input().split()))
    last_node = 0
    for item in array:
        tree.append(item)
        last_node += 1
        enqueue(last_node)
    answer = 0
    idx = N // 2
    while idx >= 1:
        answer += tree[idx]
        idx //= 2
    print(f'#{tc}',answer)



