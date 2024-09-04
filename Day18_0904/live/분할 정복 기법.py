'''
분할 정복 기법으로 거듭 제곱 문제
제곱 값이 짝수이면 2 ** n//2를 2번 곱하기

'''
def square(num,n):
    global cnt
    cnt += 1
    if n == 1:
        return num
    elif n % 2 == 0:
        y = square(num, n /2)
        return y * y
    else:
        y = square(num, (n-1)/2)
        return y * y * num
cnt = 0
answer = square(2,13)
print(answer)
print(cnt)