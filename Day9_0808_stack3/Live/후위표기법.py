def calcul(array):
    rank = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    answer =''
    for i in array:
        if i not in rank.keys():
            answer += i
        if i in rank.keys() and not stack:
            stack.append(i)
        elif i in rank.keys() and stack:
            if rank[stack[-1]] >= rank[i]:
                answer += stack.pop()
                stack.append(i)
            else:
                stack.append(i)

    while stack:
        answer += stack.pop()

    return answer


T = int(input())
for tc in range(1,T+1):
    array = list(map(str, input().split()))

