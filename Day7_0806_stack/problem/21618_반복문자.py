def same(array):
    stack = []
    for c in array:
        if c not in stack:
            stack.append(c)
        elif c in stack and c != stack[-1]:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()


    return len(stack)



T = int(input())
for tc in range(1,T+1):
    array = list(input())


    answer = same(array)
    print(f'#{tc} {answer}')