class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        start = 0
        e = n-1
        while(start<e):
            temp = s[start]
            s[start]=s[e]
            s[e]=temp
            start+=1
            e-=1

        