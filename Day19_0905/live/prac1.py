# 1~10의 부분집합 중 원소의 합이 10인 부분집합을 모두 출력하시오
arr = [1,2,3,4,5,6,7,8,9,10]
path = []

# 버전2
# 이진 트리처럼 사용(후보 사용 vs 사용 x)하면 훨씬 쉽고 빠르다
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(path)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    path.append(arr[level]) # 경로 저장용
    dfs2(level + 1, sum + arr[level])
    path.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)