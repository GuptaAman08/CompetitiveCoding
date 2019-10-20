from sys import stdin

t = int(stdin.readline())

while t:
    n, bob, alice = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]

    temp = []
    n_m_a, n_m_b = 0, 0

    for i in a:
        if i%alice == 0 and i%bob == 0:
            n_m_b = 1
        else:
            temp.append(i)

    if temp:
        for i in temp:
            if i % alice == 0:
                n_m_a += 1

            if i%bob == 0:
                n_m_b += 1
                    
    if n_m_b > n_m_a:
        print('BOB')
    else:
        print('ALICE')

    t -= 1