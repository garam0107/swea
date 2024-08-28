def hap_tree(array,N):
    for i in range(N,0,-1):
        if array[i] == 0:
            if i*2 <= N:
                array[i] += array[i*2]
            if i*2+1 <= N:
                array[i] += array[i*2+1]
    return array



T = int(input())
for tc in range(1,T+1):
    node_N, leaf_M, node_num = list(map(int,input().split()))
    tree = [0] *(node_N+1)
    for _ in range(leaf_M):
        leaf_idx,leaf_num = map(int,input().split())
        tree[leaf_idx] = leaf_num
    hap_tree(tree,node_N)
    answer = tree[node_num]
    print(f'#{tc} {answer}')




