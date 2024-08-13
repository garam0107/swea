queue = [1,2,3]
queue.append(4)
queue.append(5)

queue.pop(0)
queue.pop(0)

N = 10
Q= [0] * N
front = -1
rear = -1

rear += 1
Q[rear] = 1
rear += 1
Q[rear] = 2
rear += 1
Q[rear] = 3

front += 1
print(Q[front])
front += 1
print(Q[front])
front += 1
print(Q[front])


