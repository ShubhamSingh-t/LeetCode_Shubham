class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        result = [-1] * n  # Initialize result list
        Max = -1  # Start with -1 since the last element always gets -1
        
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            result[i] = Max  # Replace current element
            Max = max(Max, arr[i])  # Update maximum
        
        return result
        