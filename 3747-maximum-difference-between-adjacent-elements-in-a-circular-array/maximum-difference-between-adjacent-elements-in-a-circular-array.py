class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n =  len(nums)
        m = abs(nums[n-1] - nums[0])
        for i in range(n-1):
            m = max(abs(nums[i]-nums[i+1]), m)
        return m

        

        

        


        