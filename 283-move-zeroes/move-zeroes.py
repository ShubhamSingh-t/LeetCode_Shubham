class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n  = len(nums)
        s = 0
        for i in range (n):
            if(nums[i]!=0):
                nums[s] = nums[i]
                s+=1

        for i in range(s, n):
            nums[i]=0
            


        