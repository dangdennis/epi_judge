from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = []
    maybe_primes = [False, False] + [True] * (n - 1)
    
    for i in range(2, len(maybe_primes)):
        if maybe_primes[i]:
            primes.append(i)
            
            for j in range(i, len(maybe_primes), i):
                maybe_primes[j] = False
            
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
