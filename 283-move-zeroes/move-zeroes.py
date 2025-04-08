class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s = 0

   
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != s:
                    nums[s], nums[i] = nums[i], nums[s]
                s += 1
        return nums
        