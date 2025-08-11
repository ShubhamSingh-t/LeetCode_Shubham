class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        Max , Min = nums[0], nums[0]
        res = Max
        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(curr, curr*Min, curr*Max)
            Min = min(curr, curr*Min, curr*Max)
            Max = temp
            res = max(res, Max)
        return res
