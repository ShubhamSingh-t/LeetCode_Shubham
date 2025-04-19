class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Sum = sum(nums)
        left = 0
        for i in range(len(nums)):
            left = (left+nums[i])-nums[i]
            if left == (Sum-left-nums[i]):
                return i
            left += nums[i]
            
        return -1

        