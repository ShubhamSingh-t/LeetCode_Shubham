class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans = 0
        prefix = list(itertools.accumulate(nums))
        suffix = list(itertools.accumulate(nums[::-1]))[::-1]

        for i, num in enumerate(nums):
            if num > 0:
                continue
            if prefix[i] == suffix[i]:
                ans += 2  
            if abs(prefix[i] - suffix[i]) == 1:
                ans += 1 
        return ans