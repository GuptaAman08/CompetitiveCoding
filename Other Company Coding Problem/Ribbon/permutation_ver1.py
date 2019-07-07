# This code is non-recursive implementation of generating all permutation of a string
import queue, sys

in_string = input()
c = 0
for i in in_string:
    q = queue.Queue(maxsize=sys.maxsize)
    q.put(i)
    copy_instring = in_string
    while not(q.empty()):
        temp = q.get()
        # print(list(q.queue))
        if len(temp) == len(in_string):
            print(temp)
            c += 1
        else:
            copy_instring = in_string
            for i in temp:
                copy_instring = copy_instring.replace(i, "")
            for i in copy_instring:
                q.put(temp + i)

print(c)