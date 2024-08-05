def ctrl_f(array, word):
    r = len(word)
    counts = 0
    for i in range(len(array)-r):
        text = []
        for k in range(r):
            text += array[i+k]
            if text == word:
                counts += 1
    return counts
for _ in range(10):
    tc = int(input())
    word = list(map(str, input()))
    array = list(map(str, input()))

    answer = ctrl_f(array,word)
    print(f'#{tc} {answer}')