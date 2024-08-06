def match_number(array):
    stack = []
    for c in array:
        if c not in stack:
            stack.append(c)
        elif c in stack and c != stack[-1]:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()
    return stack

#
T = 10
for tc in range(1, T+1):
    N, array = input().split()
    answer = ''.join(map(str, match_number(array)))
    print(f'#{tc} {answer}')