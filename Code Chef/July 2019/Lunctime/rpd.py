t = int(input())

while t:
    n = int(input())
    arr = [int(x) for x in input().split()]

    def calc_sum_digits(num):
        s = 0
        while num:
            rem = num % 10
            num = num // 10
            s += rem 
        return s

    max_prod = float('-inf')
    for i in range(n):
        for j in range(i+1, n):
            temp = calc_sum_digits(arr[j]*arr[i])
            if temp > max_prod:
                max_prod = temp
                
    print(max_prod)
    t -= 1
        
        
        
