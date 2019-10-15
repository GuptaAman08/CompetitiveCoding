t = int(input())

while t:
    n = int(input())
    p = [int(x) for x in input().split()]

    count = 1
    track = [p[0]]


    if p[1] < min(track):
        count += 1
    track.append(p[1])

    if p[2] < min(track):
        count += 1
    track.append(p[2])

    if p[3] < min(track):
        count += 1
    track.append(p[3])

    if p[4] < min(track):
        count += 1
    track.append(p[4])

    for i in range(5, n):
        if p[i] < min(track):
            count += 1
        track.pop(0)
        track.append(p[i])
        
    print(count)
    t -= 1
