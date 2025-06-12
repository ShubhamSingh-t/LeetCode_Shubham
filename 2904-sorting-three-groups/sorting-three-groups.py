class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = 0
        b, c = inf, inf
        for i in nums:
            a, b, c = a + (i!=1), min(a,b)+ (i!=2), min(a,b,c)+(i!=3)
        return min(a, b, c)
        
        