class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=list(s.split())
        b=a[-1]
        return len(b)