class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = 0
        for i in range (len(arr)-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1 :
               
                return True
        return False

        


        