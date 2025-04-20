class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        arr = [0, 0]
        Max = 0
        for i in range(len(mat)):
            for j in range (len(mat[0])):
                if mat[i][j]>Max:
                    Max=mat[i][j]
        for i in range(len(mat)):
            for j in range (len(mat[0])):
                if Max==mat[i][j]:
                    arr[0]=i
                    arr[1]=j
        return arr
                

        

        