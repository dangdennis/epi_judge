from audioop import reverse
from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # if len(perm) < 2:
    #     return perm
    
    # inv_idx = -1
    
    # for i in range(len(perm)-1, 0, -1):
    #     if perm[i] < perm[i-1]:
    #         # print('pair', i, perm[i])
    #         inv_idx = i

    # if inv_idx <= -1:
    #     return []
    
    # print('\n')
    # print('inv_idx',inv_idx)
        
    # for i in range(len(perm)-1, inv_idx, -1):
    #     print('trip', i, perm[i], perm[inv_idx])
    #     if perm[i] > perm[inv_idx]:
    #         perm[i], perm[inv_idx] = perm[inv_idx], perm[i]
    #         break
        
    # perm[inv_idx + 1:] = reversed(perm[inv_idx + 1:])
    
    # return perm

    inv_point = len(perm)-2
    
    while inv_point >= 0 and perm[inv_point] >= perm[inv_point + 1]:
        inv_point -= 1

    if inv_point <= -1:
        return []

    for i in reversed(range(inv_point + 1, len(perm))):
        if perm[i] > perm[inv_point]:
            perm[i], perm[inv_point] = perm[inv_point], perm[i]
            break
        
    perm[inv_point + 1:] = reversed(perm[inv_point + 1:])
    
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
