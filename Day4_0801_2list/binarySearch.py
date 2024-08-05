def binarySearch(lst,N,key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        if lst[middle] == key:
            return True
        elif lst[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False


numList = [1,2,3,4,5,6,7,8,10,13,14,15,16,19,20,22,23,24,25,26,27,28,29,30]
num = 2

print(binarySearch(numList, len(numList), num))

