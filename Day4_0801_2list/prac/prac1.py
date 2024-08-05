def selectionSort(arr, N): # arr 정렬대상, N 크기
    for i in range(N-1): # 주어진 구간에 대해서 기준 위치 i를 정한다
        min_idx = i      # 최솟값의 위치를 기준위치로 가정
        for j in range(i+1, N): #남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]: # 가정한 최솟값의 위치랑 j의 위치를 비교하고
                min_idx = j           # 가정한 최솟값의 위치의 값이 더 크다면
        arr[i],arr[min_idx] = arr[min_idx],arr[i]  # 구간의 최솟값의 위치를 교환
    return arr
A = [2, 7, 5, 3, 4, 0]
B = [1,4,5,5,6,7,8,9,13,1,4]
print(selectionSort(A, len(A)))
print(selectionSort(B, len(B)))

