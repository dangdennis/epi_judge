import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    
    # solution 1 O(n) time, O(n) space
    # ls, eq, gt = [], [], []

    # for i in A:
    #     if i < pivot:
    #         ls.append(i)
    #     elif i > pivot:
    #         gt.append(i)
    #     else:
    #         eq.append(i)

    # i = 0
    # for num in ls:
    #     A[i] = num
    #     i = i+1
        
    # for num in ls:
    #     A[i] = num
    #     i = i+1

    # for num in ls:
    #     A[i] = num
    #     i = i+1
    
    # solution 2 O(n) time, O(1) space
    # iterate first pass forward swapping all lesser values before pivot
    # iterate again from back swapping all greater values after pivot
    
    # smaller = 0
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[i], A[smaller] = A[smaller], A[i]
    #         smaller += 1
            
    # larger = len(A) - 1
    # for i in reversed(range(len(A))):
    #     if A[i] > pivot:
    #         A[i], A[larger] = A[larger], A[i]
    #         larger -= 1
    
    # solution 3 O(n) time, O(n) space
    # one pass only
    ls, eq, gt = 0, 0, len(A)-1
    
    while eq <= gt:
        if A[eq] < pivot:
            A[ls], A[eq] = A[eq], A[ls]
            ls, eq = ls + 1, eq + 1
        elif A[eq] == pivot:
            eq += 1
        else:
            A[gt], A[eq] = A[eq], A[gt]
            gt -= 1
            
    
    
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
