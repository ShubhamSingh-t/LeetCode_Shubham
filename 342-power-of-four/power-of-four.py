class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <1:
            return False
        while n>=1:
            if n > 1:
                n = n/4

            elif n==1:
                return True
        return False

        