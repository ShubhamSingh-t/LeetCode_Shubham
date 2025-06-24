class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        count = 0

        for j in range(n):
            less_left = greater_left = 0
            less_right = greater_right = 0

            
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                elif rating[i] > rating[j]:
                    greater_left += 1

           
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    greater_right += 1
                elif rating[k] < rating[j]:
                    less_right += 1

           
            count += (less_left * greater_right) + (greater_left * less_right)

        return count
            