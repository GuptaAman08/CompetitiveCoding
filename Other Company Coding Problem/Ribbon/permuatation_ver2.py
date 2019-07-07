# This code uses python inbuilt module itertools to generate all permutation
# Itertool is in-built in python

from itertools import permutations
# Refer HackerRank link (https://www.hackerrank.com/challenges/itertools-permutations/problem) for this  


in_string = input()
# The second argument in permutations specify the all possible permutations of that length
a = list(permutations(in_string, len(in_string)))
for i in range(len(a)):
    a[i] = ''.join(a[i])

print(*a)