class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0     
        value = 0    
        weight = 1    

       
        count += s.count('0')

        
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if weight <= k and value + weight <= k:
                    value += weight
                    count += 1
                else:
                    continue
            weight *= 2
            if weight > k:  
                break

        return count
            