class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        while n>=1:
            if n==1:
                return True
            else:
                n=n/3
        return False

        