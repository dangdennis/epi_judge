import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    # O(n) time, O(n) space
    # known_vals = {}
    # for i in range(len(A)):
    #     key = A[i]
    #     known_vals[key] = True
    
    # for i, v in enumerate(known_vals):
    #     A[i] = v
        
    # for i in range(len(known_vals.keys()), len(A)):
    #     A.pop()
    
    # return len(A)
    
    # O(n) time, O(1) space
    vacant_index = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            A[vacant_index] = A[i]
            vacant_index += 1
    
    for _ in range(vacant_index, len(A)):
        A.pop()
        
    return len(A)

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
