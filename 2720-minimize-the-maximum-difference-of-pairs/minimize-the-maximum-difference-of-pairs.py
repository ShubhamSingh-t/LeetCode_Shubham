class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        def can_form(max_diff):
            pairs = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    pairs += 1
                    i += 2  # skip this pair
                else:
                    i += 1  # try next element
            return pairs >= p
        
        low, high = 0, nums[-1] - nums[0]
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_form(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans