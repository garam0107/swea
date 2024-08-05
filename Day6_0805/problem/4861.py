def mysort(arr):
    return arr[::-1]
def reverse(arr):
    if arr == mysort(arr):
        return arr



T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    array = [list(map(int, input()))]
    answer = ''
    for i in range(N):
        if array[i][0:M] == mysort(array[i][0:M]):
            print(array[i][0:M])
