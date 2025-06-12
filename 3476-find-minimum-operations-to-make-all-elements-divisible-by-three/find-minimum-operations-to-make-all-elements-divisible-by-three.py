class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        for i in range (n):
            if nums[i]%3 ==1:
                nums[i]-=1
                c+=1
            elif nums[i]%3 ==2:
                nums[i]+=1
                c+=1
        return c
        