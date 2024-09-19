class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=min(strs,key=len)
        l=len(s)
        for i in strs:
            while not (i.startswith(s[0:l])):
                l-=1
        return s[0:l]
        