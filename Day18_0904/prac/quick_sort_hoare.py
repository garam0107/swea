'''
hoare 방식의 퀵 정렬
'''

# 호어 방식의 배열 쪼개기
def hoare_partition(left,right):
    pivot = arr[left]
    left += 1
    '''
     left         right
      ↓             ↓   
    3 2 4 6 9 1 8 7 5
    ↑
    p
    '''
    while True:
        # left index가 right index보다 작고
        while left <= right and arr[left] < pivot:
            # left번 째 값이 pivot보다 작다면
            left += 1

        while left <= right and arr[right] > pivot:
            right -= 1
        if left >= right:
            '''
            조사 진행중 left와 right가 엇갈린 상황이 발생한다면
            left,right 두 위치를 swap하지 않고 right 자리를 return
            '''
            return right    # pivot_index
        arr[left],arr[right] = arr[right],arr[left]


'''
left : 왼쪽 정렬 대상 시작 지점
right : 오른쪽 정렬 대상 시작 지점
'''
def quick_sort(left,right):
    # 조사 대상이 하나 이하가 되면 더 이상 조사할 요소가 없기에 종료
    if left >= right : return
    '''
    호어 방식의 정렬을 위해서는, 정렬을 위한 배열을
    영역별로 구분 지을 수 있어야 하고, 호어 방식의 파티션 구분 결과로 
    얻은 index 지점을 pivot으로 지정
    '''
    pivot_index = hoare_partition(left,right)
    arr[left],arr[pivot_index] = arr[pivot_index],arr[left]

    quick_sort(left,pivot_index - 1)
    quick_sort(pivot_index + 1, right)

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0,len(arr)-1)
print(arr)