#from math import comb
class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        
        MOD = 10**9 + 7
        if k > n - 1:

            return 0
        if k == 0:
            return m if n == 1 else (m * pow(m - 1, n - 1, MOD)) % MOD

        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def nCr(a, b):
            if b > a or b < 0:
                return 0

            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        ways_to_choose_k = nCr(n - 1, k)
        ways_to_fill_remaining = pow(m - 1, n - 1 - k, MOD)

        total_good_arrays = (ways_to_choose_k * m) % MOD
        total_good_arrays = (total_good_arrays * ways_to_fill_remaining) % MOD
        
        return total_good_arrays