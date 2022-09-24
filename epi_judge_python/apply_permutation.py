from time import perf_counter_ns
from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # O(n) space and time
    # permutated = [0] * len(A)
    # for i in range(0, len(A)):
    #     pos = perm[i]
    #     permutated[pos] = A[i]

    # for i in range(0, len(A)):
    #     A[i] = permutated[i]
    
    # O(n) time and O(1) space
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] = -1
            next = temp

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
