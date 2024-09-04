'''
left = 1
right = 2
'''


def binary_search(x,start,end,now):
    global cnt
    mid = (start+end) // 2


    if x == list_a[mid]:
        cnt += 1
    if start > end:
        return

    if x < list_a[(start+end)//2]:
        if now == 2:
            binary_search(x,start,mid-1,1)
        else:
            return
    elif x > list_a[(start+end)//2]:
        if now == 1:
            binary_search(x,mid+1,end,2)
        else:
            return





T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_a.sort()
    cnt = 0
    for i in list_b:
        if i > list_a[(0+len(list_a)-1) //2]:
            binary_search(i,0,len(list_a)-1,2)
        else:
            binary_search(i,0,len(list_a)-1,1)
    print(f'#{tc} {cnt}')


