from typing import List
import math

class Solution:
    @staticmethod
    def steps_to_zero(x: int) -> int:
        if x == 0:
            return 0
        return int(math.log(x, 4)) + 1   # O(1)

    @staticmethod
    def prefix_sum(n: int) -> int:
        """Sum of steps_to_zero(i) for i=1..n"""
        if n <= 0:
            return 0
        total = 0
        k = 0
        while (1 << (2*k)) <= n:   # 4^k = 2^(2k)
            start = 1 << (2*k)          # 4^k
            end = min(n, (1 << (2*(k+1))) - 1)  # min(n, 4^(k+1)-1)
            count = end - start + 1
            if count > 0:
                total += count * (k+1)
            k += 1
        return total

    def minOperations(self, queries: List[List[int]]) -> int:
        total_operations = 0
        for l, r in queries:
            total_steps = self.prefix_sum(r) - self.prefix_sum(l-1)
            total_operations += math.ceil(total_steps / 2)
        return total_operations
