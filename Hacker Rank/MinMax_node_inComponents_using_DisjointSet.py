n = int(input())

parent = [x for x in range(2*n)] 
set_size = [1] * (2 * n)

# path compression version of Dis Joint Set DataStructure 
def findParent(i, parent):
    if i == parent[i]:
        return parent[i]
    parent[i] = findParent(parent[i], parent)
    return parent[i]

for i in range(n):
    u, v = [int(x) for x in input().split()]
    
    pu = findParent(u-1, parent)
    pv = findParent(v-1, parent)
    
    if pu != pv:
        parent[pu] = pv 
        temp = set_size[pu] + set_size[pu]
        set_size[pu], set_size[pv] = temp, temp


min_val = float('inf')
max_val = float('-inf')

for i in range(2*n):
    if parent[i] != i:
        if set_size[i] < min_val:
            min_val = set_size[i]
        if set_size[i] > max_val:
            max_val = set_size[i]

print(min_val, max_val)




    