class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_cost = nums[:]  
        ans = sum(nums)    

        for k in range(1, n): 
            for i in range(n):
                
                min_cost[i] = min(min_cost[i], nums[(i - k + n) % n])
            
            ans = min(ans, sum(min_cost) + k * x)

        return ans