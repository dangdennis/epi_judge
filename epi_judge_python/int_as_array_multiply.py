from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = 1
    if num1[0] < 0 and num2[0] > 0:
        sign = -1
    elif num1[0] > 0 and num2[0] < 0:
        sign = -1
        
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # clever pythonic way to remove leading zeroes
    # result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]  
    
    # caveman way
    no_leading_zeros = []
    encountered_leading_zero_state = False

    for i, x in enumerate(result):
        if i == 0 and x == 0:
            encountered_leading_zero_state = True
            
        if encountered_leading_zero_state and x != 0:
            encountered_leading_zero_state = False
        
        if not encountered_leading_zero_state:
            no_leading_zeros.append(x)
            
    no_leading_zeros = no_leading_zeros or [0]
    no_leading_zeros[0] *= sign
    
    return no_leading_zeros



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
