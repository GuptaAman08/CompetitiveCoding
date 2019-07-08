from collections import defaultdict
test_cases = int(input())

def getEven(x):
    b = bin(x)
    c = len(list(filter(lambda x: x == '1', b[2:])))
    if c % 2 == 0:
        return True
    else:
        return False

while test_cases != 0:

    q = int(input())

    first = int(input())
    s = defaultdict(int)
    s[first] = 1
    count_Even = 0
    count_Odd = 0

    if getEven(first):
        count_Even += 1
    else:
        count_Odd += 1


    print(count_Even, count_Odd)
    for i in range(q-1):
        t = int(input())

        for x in list(s):
            temp = x ^ t
            if s[temp] == 0:
                s[temp] = 1
                if getEven(temp):
                    count_Even += 1
                else:
                    count_Odd += 1
        
        if s[t] == 0:
            s[t] = 1
            if getEven(t):
                count_Even += 1
            else:
                count_Odd += 1
        print(count_Even, count_Odd)
    
    test_cases -= 1
    