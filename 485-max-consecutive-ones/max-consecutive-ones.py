class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        arr = []
        for i in range(len(nums)):
            
            if nums[i]==1:
                count+=1
                arr.append(count)
            else:
                count = 0
                arr.append(count)

        return max(arr)

        