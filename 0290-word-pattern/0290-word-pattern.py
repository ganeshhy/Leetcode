class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        a=pattern
        b=str.split()
        return map(a.find,a)==map(b.index,b)