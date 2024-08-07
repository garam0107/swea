def solution(pro,sppeds):
    finish = 100
    d_day = []
    for i in range(len(pro)):
        s = (finish - pro[i]) // sppeds[i]
        if pro[i] + (s * sppeds[i]) < 100:
            s += 1
        d_day.append(s)
    return d_day

pro = [95,90,99,99,80,99]
speeds = [1,1,1,1,1,1]

answer = solution(pro,speeds)
print(answer)

A = list(map, int(input()))

print(A)
print(type(A))