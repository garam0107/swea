T = int(input())
for tc in range(1, T+1):
    P,A,B = map(int, input().split())

    bookArray = list(range(1, P+1))

    start = 1
    end = P
    countA = 0
    countB = 0

    while start <= end :
        countA += 1
        mid = (start+end) // 2
        if bookArray[mid] == A:
            print mid
        elif bookArray[mid] > A:
            mid = mid // 2
        else :
            start = mid
            mid = (start+end) // 2
    print(countA)



