from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i in range(len(nums)) if nums[i] == key]
        res = set()
        
        for i in key_indices:
            for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                res.add(j)
        
        return sorted(res)

        
            

        