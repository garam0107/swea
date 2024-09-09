T = int(input())
result = ''
for tc in range(1,T+1):
    A,B,C,D = map(int,input().split())
    light = [0] * 101
    for i in range(A,B+1):
        light[i] += 1
    for j in range(C,D+1):
        light[j] += 1

    answer = light.count(2)
    if answer == 0:
        answer = 0
    else:
        answer -= 1
    result += f'#{tc} {answer} \n'

print(result)



