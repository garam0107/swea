# s1 = list(input())
# s2 = input()
# print(s1[0])
# print(s2[0])

def strlen(a):  # for문
    mylen = 0
    for i in a:
        if i == '\0':
            pass
        else :
            mylen += 1
    return mylen
a = ['a', 'b', 'c', '\0']

print(strlen(a))


# while문

def strlen1(a):
    i = 0
    while a[i] != '\0':
        i += 1
    return i
a = ['a', 'b', 'c', '\0']

print(strlen1(a))