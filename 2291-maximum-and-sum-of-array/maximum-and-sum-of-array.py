from functools import lru_cache
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        


        n = len(nums)
        slots = numSlots

        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0

            max_sum = 0
            for slot in range(slots):
                count = (mask // (3 ** slot)) % 3
                if count < 2:
                    new_mask = mask + (3 ** slot)
                    and_value = nums[i] & (slot + 1)
                    max_sum = max(max_sum, and_value + dp(i + 1, new_mask))
            return max_sum

        return dp(0, 0)