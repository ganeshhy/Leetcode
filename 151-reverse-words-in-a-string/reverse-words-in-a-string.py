class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        b=a[::-1]
        res=" ".join(b)
        return res
        