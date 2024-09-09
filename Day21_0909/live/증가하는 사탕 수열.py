T = int(input())
for tc in range(1,T+1):
    array = list(map(int,input().split()))
    answer = 0
    for i in range(2,0,-1):
        if array[i] <= array[i-1]:
            answer += array[i-1] - array[i] + 1
            array[i-1] = array[i] - 1

        if array[i] <= 0: # 사탕을 먹고 나서 0개 이하 이면 조건 불만족이므로 -1 출력
            answer = -1
            break

    print(answer)




