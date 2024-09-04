'''
pivot 정하고 pivot 기준으로 작은 것들을 왼편에 위치
큰 것들을 오른편에 위치
'''

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]

def hoare_partition1(left, right):
    mid = (left+right) // 2
    pivot = arr[mid]  # 피벗을 제일 왼쪽 요소로 설정
    arr[left],arr[mid] = arr[mid],arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = hoare_partition1(left, right)
        # pivot = hoare_partition2(left, right)
        # pivot = hoare_partition3(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)