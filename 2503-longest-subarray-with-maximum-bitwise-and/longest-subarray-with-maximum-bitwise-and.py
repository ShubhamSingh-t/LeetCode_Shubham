class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
        m = max(nums)
        c=0
        l=0
        for i in range(n-1,-1,-1):
            if nums[i]==m:
                c+=1
                l = max(l, c)
            else:
                c=0
        return l
        