def print_all_permut(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l,r+1):
            s[l], s[i] = s[i], s[l]
            print_all_permut(s, l+1, r)
            # Backtracking to bring string in original position
            s[l], s[i] = s[i], s[l]


# This is a recursive approach for generating all permutaiton of a string
s = list(input())

# refer this video https://www.youtube.com/watch?v=d-Hl-zwxS8s
# Definition is string s , lower bound l(Which fixes positions of characters less than l) and length of string
print_all_permut(s, 0, len(s)-1)