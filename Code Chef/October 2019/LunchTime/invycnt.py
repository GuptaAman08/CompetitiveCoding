from sys import stdin

t = int(stdin.readline())

while t:
    n, k = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]

    less = 0
    final_ans = 0

    for i in range(n):
        for j in range(n):
            if j < i:
                if a[j] < a[i]:
                    less += 1
            else:
                if a[j] < a[i]:
                    final_ans += 1
    
    # print(less, greater)
    final_ans = final_ans * ((k*(k+1))//2)
    
    final_ans += less * ((k*(k-1))//2)
    print(final_ans)
    t -= 1