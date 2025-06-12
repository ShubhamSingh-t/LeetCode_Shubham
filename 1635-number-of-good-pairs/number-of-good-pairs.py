class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        res = 0
        for f in count.values():
            res += f*(f-1)//2
        return res
