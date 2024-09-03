def print_name():
    print('{',end='')
    for i in range(3):
        if path[i] == 0:
            print(name[i],end='')
    print('}')


def run(level):
    if level == 3:
        print_name()
        return

    for i in range(2):
        path.append(a[i])
        run(level+1)
        path.pop()


a = [0,1]
name = ['A','B','C']
path = []
run(0)