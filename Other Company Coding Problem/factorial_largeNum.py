def mul(x, res, res_size):
    carry = 0

    for i in range(res_size):
        prod = res[i] * x + carry
        res[i] = prod % 10
        carry = prod // 10

    while carry:
        res[res_size] = carry % 10
        carry = carry // 10
        res_size += 1
    
    return res_size

def factorial(n):
    res = [0] * 500
    res[0] = 1
    res_size = 1

    x = 2
    while x <= n:
        res_size = mul(x, res, res_size)    
        x = x + 1
    
    i = res_size - 1
    while i >= 0:
        print(res[i], end='')
        i -= 1

n = int(input())
factorial(n)