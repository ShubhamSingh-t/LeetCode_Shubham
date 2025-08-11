class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        s=0
        e=n-1
        ans = nums[0]
        if n==1:
            return nums[0]
        while s<=e:
            if nums[s]<nums[e]:
                ans =min(ans, nums[s])
            m = (s+e)//2
            ans = min(nums[m], ans)
            if nums[s]<=nums[m]:
                s = m+1
            else:
                e = m-1
        return ans
