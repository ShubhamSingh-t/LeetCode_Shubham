class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1]*n
        pre, pos = 1, 1
        for i in range(n):
            arr[i]=pre
            pre = pre*nums[i]
        for i in range(n-1, -1, -1):
            arr[i] = arr[i]*pos
            pos = pos*nums[i]
        return arr
        
        