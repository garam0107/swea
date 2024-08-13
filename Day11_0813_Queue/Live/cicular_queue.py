cQ = [0] * 4
front = rear = 0

rear = (rear+1) % len(cQ) # enq(1)
cQ[rear] = 1

rear = (rear+1) % len(cQ) # enq(1)
cQ[rear] = 2

rear = (rear+1) % len(cQ) # enq(1)
cQ[rear] = 3

front = (front+1) % len(cQ)
print(front)
print(cQ[front])
front = (front+1) % len(cQ)
print(front)
print(cQ[front])
front = (front+1) % len(cQ)
print(front)
print(cQ[front])