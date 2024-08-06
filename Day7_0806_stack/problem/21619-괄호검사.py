def match(array):
    stack = []
    search =['(',')']
    for c in array:
        if c == search[0]:
            stack.append(c)
        elif c == search[1]:
            if not stack:
                 return False
            stack.pop()

    return not stack
T = int(input())
for tc in range(1,T+1):
    array = input()
    if match(array):
        print(1)
    else:
        print(-1)