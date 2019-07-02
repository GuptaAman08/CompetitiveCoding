t=int(input())

# Got Error with this of maximum recursion depth reached 
def find_road_sign(k):
    if k == 1:
        return 10
    return 2 * find_road_sign(k-1)

for _ in range(t):
    k = int(input())
    ans = find_road_sign(k)
    print(ans % 1000000007)

    