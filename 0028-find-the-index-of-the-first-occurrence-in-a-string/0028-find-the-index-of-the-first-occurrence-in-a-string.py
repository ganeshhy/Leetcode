class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length=len(needle)
        for i in range(len(haystack)):
            t=haystack[i:length+i]
            if t==needle:
                return i
        return -1