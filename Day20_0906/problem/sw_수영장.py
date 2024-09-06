'''
month: 현재 달
sum_cost: 경우의 수마다 누적시킨 비용 합
'''


def dfs(month,sum_cost):
    pass
'''
'''


T = int(input(0))
for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    array = [0] + list(map(int, input().split())) # 1월부터 12월 쓰기 위함



# dp 버전
'''
현재 달의 최소 비용 계산
이전 달 최소 비용과 현재 달의 최소 비용을 계속 더해주면서 진행
경우의 수는 이전 달 + 1일권 구입, 이전 달 + 한달권, 이전 달+ 3개월 치

'''


T = int(input())
for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    array = [0] + list(map(int, input().split())) # 1월부터 12월 쓰기 위함
    dp = [0] * 13 # 1~12월 최소 금액 저장

    for i in range(1,13):


