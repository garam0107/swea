# 파이썬 방식 quick_sort
def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0]
        down,up,equal = [],[],[]
        for i in range(1,len(div_arr)):
            if div_arr[i] < pivot:
                down.append(div_arr[i])
            elif div_arr[i] == pivot:
                equal.append(div_arr[i])
            else:
                up.append(div_arr[i])

    return quick_sort(down) + equal + quick_sort(up)





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    array = list(map(int, input().split()))
    answer = quick_sort(array)
    print(f'#{tc} {answer[N//2]}')