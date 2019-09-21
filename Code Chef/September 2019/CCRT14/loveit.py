v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
a = input()

while a != '0':
    s = a.split()
    t = []
    for x in s:
        if x[0] in v:
            t.append('T' + x.lower())
        else:
            t.append('T' + x[1:].lower())
    
    print(' '.join(t))
    a = input()
