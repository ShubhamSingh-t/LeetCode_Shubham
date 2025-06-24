import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]  
        heapq.heapify(max_heap)
        
        s = 0
        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            s += max_val
            heapq.heappush(max_heap, -ceil(max_val / 3))
            
        return s


            