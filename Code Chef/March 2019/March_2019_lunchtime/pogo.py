t = int(input())

while t != 0:
    list_a = [int(x) for x in input().split()]
    n, k = list_a

    list_b = [int(x) for x in input().split()]

    if n == k:
        cur_max = max(list_b)
    else:
        dist_first_k_ele = []
        for i in range(k):
            dist_first_k_ele.append(sum(list_b[i:len(list_b):k]))

        cur_max = max(dist_first_k_ele)
        for i in range(k, len(list_b)):
            dist_first_k_ele[i%k] = dist_first_k_ele[i%k] - list_b[i-k]
            if cur_max < dist_first_k_ele[i%k]:
                cur_max = dist_first_k_ele[i%k]

    t -= 1    
    print(cur_max)

