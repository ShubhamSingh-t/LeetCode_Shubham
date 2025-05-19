class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = 0
        C = 0
        CE = 0
        for i in range(len(nums)-1):
            M = max(M, i+nums[i])
            if i==CE:
                C+=1
                CE = M
        return C
