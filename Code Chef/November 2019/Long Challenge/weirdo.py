from sys import stdin
from collections import Counter
import math
from string import ascii_lowercase

vowels = ['a', 'e', 'i', 'o', 'u']

def Alorbob(l2, temp):
    for j in range(l2-2):
        if (temp[j] in vowels) and (temp[j+1] not in vowels) and (temp[j+2] not in vowels):
            return 1
        elif (temp[j] not in vowels) and (temp[j+1] in vowels) and (temp[j+2] not in vowels):
            return 1
        elif (temp[j] not in vowels) and (temp[j+1] not in vowels) and (temp[j+2] in vowels):
            return 1
        elif (temp[j] not in vowels) and (temp[j+1] not in vowels) and (temp[j+2] not in vowels):
            return 1

    return 0


t = int(stdin.readline())

while t:
    l1 = int(stdin.readline())
    s = [stdin.readline().strip() for i in range(l1)]

    fxcA = Counter()
    xcA = Counter()

    fxcB = Counter()
    xcB = Counter()

    ca, cb = 0, 0
    for i in range(l1):
        temp = s[i]
        l2 = len(temp)

        if l2 == 2:
            if (temp[0] not in vowels) and (temp[1] not in vowels):
                fxcB += Counter(temp)
                xcB += Counter(set(temp))
                cb += 1
            else:
                fxcA += Counter(temp)
                xcA += Counter(set(temp))
                ca += 1
        else:     
            if Alorbob(l2, temp):
                fxcB += Counter(temp)
                xcB += Counter(set(temp))
                cb += 1
            else:
                fxcA += Counter(temp)
                xcA += Counter(set(temp))
                ca += 1

    # print(xcA, xcB, fxcA, fxcB)


    nA = sum([math.log10(v) for k, v in xcA.items()])
    nB = sum([math.log10(v) for k, v in xcB.items()])


    dA = sum([math.log10(v) for k, v in fxcA.items()])
    dB = sum([math.log10(v) for k, v in fxcB.items()])

    scA = nA - (ca*dA)
    scB = nB - (cb*dB)

    ans = scA - scB
    if ans > 7.0:
        print('Infinity')
    else:
        print(pow(10, ans))


    t -= 1