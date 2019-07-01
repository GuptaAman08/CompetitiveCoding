import sys, queue
n = 7

q = queue.Queue(maxsize=sys.maxsize)
q.put('9')

s = 0
while True:
    s = int(q.get())

    if (s % n) == 0:
        break
    
    q.put(str(s) + '0')
    q.put(str(s) + '9')

print(s)

# This version caused TimeOut for Last Test Case(Case 10)