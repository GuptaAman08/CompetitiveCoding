from collections import defaultdict

t = int(input())

while t:
    n = int(input())
    l = []
    final_dict = defaultdict(int)
    for i in range(n):
        temp = ''

        s = input()
        temp += '1' if 'a' in s else '0'
        temp += '1' if 'e' in s else '0'
        temp += '1' if 'i' in s else '0'
        temp += '1' if 'o' in s else '0'
        temp += '1' if 'u' in s else '0'
        final_dict[temp] += 1


    final_dict_keys = list(final_dict.keys())
    
    final_ans = 0
    if final_dict['11111'] > 1:
        final_ans += ((final_dict['11111'] - 1)* final_dict['11111']) // 2

    for ind, i in enumerate(final_dict_keys):
        for j in final_dict_keys[ind+1:]:
            if (int(i, 2) | int(j, 2)) == 31:
                final_ans += final_dict[i] * final_dict[j]
    print(final_ans)

    t -= 1

