# 중복 호출을 줄이기 위한 메모이제이션 방법
def fibo1(n):
    global memo
    if n >=2 and memo[n]==0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]


n = 1000
memo = [0] * (n+1)
memo[0] = 1
memo[1] = 1
print(fibo1(200))