class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s2=s.strip()
        words = s2.split()
        rev=words[::-1]
        reversed= " ".join(rev)
        return reversed
        