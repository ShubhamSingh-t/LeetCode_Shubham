class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = -10
        for i in range (n-1, 0, -1):
            for j in range(i-1, -1, -1 ):
                if nums[i]-nums[j]>m:
                    m = nums[i]-nums[j]
        if m <= 0:
            return -1

        return m
