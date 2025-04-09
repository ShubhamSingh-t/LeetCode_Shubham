class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = 0
        e = len(nums)-1
        while(s<=e):
            mid = (s+e)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                s = mid+1
            else:
                e=mid-1

        return s
            
        


        