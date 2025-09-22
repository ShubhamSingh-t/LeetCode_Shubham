class Solution:
    from collections import Counter

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        return sum(count for count in freq.values() if count == max_freq)
