def cube(x,total):
    global cnt
    if total > 10:
        return
    if x == 3:
        cnt+=1
        print(final)
        return
    for i in range(1,7):
        final.append(i)
        cube(x+1,total+i)
        final.pop()


final = []
cnt = 0
cube(0,0)
print(cnt)