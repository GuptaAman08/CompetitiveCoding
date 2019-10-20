import random

f=open('output.txt','w')

def test():
    t=random.randint(1,10)
    f.write(str(t) + "\n")
    for i in range(t):
        n=random.randint(1,100)
        a=random.randint(1,50)
        b=random.randint(1,50)

        f.write(str(n) + " ")
        f.write(str(a) + " ")
        f.write(str(b) + "\n")
        for i in range(n):
            m=random.randint(1, 100)
            f.write(str(m) + " ")
        f.write("\n")
test()
f.close()