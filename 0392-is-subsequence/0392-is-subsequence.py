class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s)==0):
            return True
        j=0
        for i in t:
            if (s[j]==i):
                j+=1
            if  j==len(s):
                return True
        return False
        