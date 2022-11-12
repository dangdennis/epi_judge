from typing import List

import math
from test_framework import generic_test


def has_duplicates(blocks: List[int]) -> bool:
    blocks = list(filter(lambda x: x != 0, blocks))
    return len(blocks) != len(set(blocks))


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    n = len(partial_assignment)
    if any(
        has_duplicates([partial_assignment[i][j] for j in range(n)])
        or has_duplicates([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False

    region_size = int(math.sqrt(n))
    return all(
        not has_duplicates(
            [
                partial_assignment[a][b]
                for a in range(region_size * i, region_size * (i + 1))
                for b in range(region_size * j, region_size * (j + 1))
            ]
        )
        for i in range(region_size)
        for j in range(region_size)
    )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
