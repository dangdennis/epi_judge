import functools
import itertools
import random
from typing import Iterator, List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


# Assumption: there are at least k elements in the stream.
def online_random_sample(stream: Iterator[int], k: int) -> List[int]:
    # my version. O(n) time, O(n) space
    # sample = []
    
    # for i in range(k):
    #     sample.append(next(stream))
    
    # total_count = k
    
    # for i in stream:
    #     total_count += 1
    #     r = random.randint(0, total_count - 1)
        
    #     if r <= k-1:
    #         sample[r] = i
    
    # return sample
    
    # official version. ~33% faster b/c appending and randint are slower than their islice and randrange equivalent
    sample = list(itertools.islice(stream, k))
    
    total_count = k
    for i in stream:
        total_count += 1
        r = random.randrange(total_count)
        if r < k:
            sample[r] = i
            
    return sample


@enable_executor_hook
def online_random_sample_wrapper(executor, stream, k):
    def online_random_sample_runner(executor, stream, k):
        results = executor.run(
            lambda:
            [online_random_sample(iter(stream), k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(len(stream), k)
        stream = sorted(stream)
        comb_to_idx = {
            tuple(compute_combination_idx(stream, len(stream), k, i)): i
            for i in range(binomial_coefficient(len(stream), k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(online_random_sample_runner, executor, stream, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_sampling.py',
                                       'online_sampling.tsv',
                                       online_random_sample_wrapper))
