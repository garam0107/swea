def per(x):

    if x == 3: # 재귀호출을 종료할 기저조건
        print(final)
        return
    # 후보군 반복
    for i in range(1,4):

        # 아래 코드의 단점: "in" - 시간 복잡도 O(N)- final 배열의 길이 만큼 탐색하기 때문에 시간복잡도가 높다
        # if i in final: # 시간 초과 위험도가 높음
        #     continue
        if visited[i]:
            continue

        # 재귀 호출 전 - 경로 기록과 사용 기록
        visited[i] = 1
        final.append(i)
        # 다음 재귀 호출(파라미터 전달)
        per(x+1)
        # 재귀 호출 종료 후 돌아왔을 때 - 사용했던 경로 삭제
        final.pop()
        visited[i] = 0



final = []
visited = [0] * 7
per(0)