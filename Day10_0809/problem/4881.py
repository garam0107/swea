def mysort(array,N):
    for i in range(N):
        for j in range(0, N-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
def minsum(array):
    col_list = []
    for i in range(N):
        col = []
        for j in range(N):
            col += [array[j][i]]
        col_list.append(mysort(col,N))
    print(col_list)
    minsum = []
    for idx in range(N):
        if col_list[idx][0] not in minsum:
            minsum.append(col_list[idx][0])
        elif col_list[idx][0] in minsum:
            for jdx in range(1,N):
                if col_list[idx][jdx] not in minsum:
                    minsum.append(col_list[idx][jdx])
                    break
    return sum(minsum)






T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    print(minsum(array))
