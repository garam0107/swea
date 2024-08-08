def forth(array):
    stack =[]
    A = ['+', '*', '/', '-']
    for c in array:
        answer = []
        if c.isdigit():
            stack.append(c)
        elif c in A and len(stack) < 2:
            return 'error'
        elif c == '+':
            for _ in range(2):
                answer.append(stack.pop())
            stack.append(int(answer[0]) + int(answer[1]))
        elif c == '*':
            for _ in range(2):
                answer.append(stack.pop())
            stack.append(int(answer[0]) * int(answer[1]))
        elif c == '-':
            for _ in range(2):
                answer.append(stack.pop())
            stack.append(int(answer[0]) - int(answer[1]))
        elif c == '/':
            for _ in range(2):
                answer.append(stack.pop())
            stack.append(int(answer[0]) // int(answer[1]))
        elif c == '.':
            if not stack:
                return 'error'
            else:
                return stack[-1]

    return stack
T = int(input())
for tc in range(1,T+1):
    array = input().split()

    print(f'#{tc} {forth(array)}')
