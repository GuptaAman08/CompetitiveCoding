t = int(input())

while t != 0:
    try:
        n = int(input())
        k = int(input())

        permut = []
        sum_max = 0
        if ((n < k) and (k%n) == 0) or (n==k):
            sum_max = 0
        elif n > k: 
            permut = [1] * k
            for i in range(n-k):
                permut.append(0)
            
            if k >= (n-k):
                ans = []
                for i in range(int(n/2)):
                    ans.append(permut[i])
                    ans.append(permut[n-i-1])
                if (n % 2) != 0:
                    ans.append(permut[int(n/2)])
                
                for i in range(len(ans)-1):
                    sum_max += abs(ans[i] - ans[i+1])
            else:
                ans = []
                for i in range(int(n/2)):
                    ans.append(permut[n-i-1])
                    ans.append(permut[i])
                if (n % 2) != 0:
                    ans.append(permut[int(n/2)])
                
                for i in range(len(ans)-1):
                    sum_max += abs(ans[i] - ans[i+1])
        else:
            a = int(k/n)
            b = k%n
            permut = [a] * (n)
            for i in range(b):
                permut[i] += 1
            
            if b >= (n-b):
                ans = []
                for i in range(int(n/2)):
                    ans.append(permut[i])
                    ans.append(permut[n-i-1])
                if (n % 2) != 0:
                    ans.append(permut[int(n/2)])
                
                for i in range(len(ans)-1):
                    sum_max += abs(ans[i] - ans[i+1])
            else:
                ans = []
                for i in range(int(n/2)):
                    ans.append(permut[n-i-1])
                    ans.append(permut[i])
                if (n % 2) != 0:
                    ans.append(permut[int(n/2)])
                
                for i in range(len(ans)-1):
                    sum_max += abs(ans[i] - ans[i+1])
                
        t -= 1
        print(sum_max)
    except Exception as e:
        print(e)
