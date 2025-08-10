class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter

        def digit_count(x):
            return Counter(str(x))

        n_count = digit_count(n)

        for i in range(31):  
            power = 1 << i
            if digit_count(power) == n_count:
                return True
        return False

            