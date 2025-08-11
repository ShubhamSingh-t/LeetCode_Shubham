from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Extract powers of 2 present in n
        powers = []
        for i in range(32):
            if (n >> i) & 1:
                powers.append(1 << i)
        
        # Precompute prefix products for optimization
        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)
        
        # Answer each query using prefix products
        result = []
        for l, r in queries:
            prod = (prefix[r + 1] * pow(prefix[l], MOD - 2, MOD)) % MOD
            result.append(prod)
        
        return result