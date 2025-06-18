class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        i = 0
        while i < n:
            group= nums[i:i+3]
            if len(group)<3:
                return []
            if group[2] - group[0] <=k:
                res.append(group)
                i+=3
            else:
                return []
        return res