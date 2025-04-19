class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        h = len(matrix)*len(matrix[0])-k
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])
            arr.sort()
                    

        return arr[len(arr)-(h+1)]

        