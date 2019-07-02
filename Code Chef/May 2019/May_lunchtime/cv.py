t = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']

while t!=0:
    n = int(input())
    s = input()
    if n == 1:
        print(0)
    else:
        count = 0
        prev = s[0]
        for i in range(1, n):
            if s[i] in vowel and prev not in vowel:
                count += 1
            prev = s[i]
        print(count)
    t -= 1

