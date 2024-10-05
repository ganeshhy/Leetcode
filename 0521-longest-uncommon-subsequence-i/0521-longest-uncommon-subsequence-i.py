class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a!=b:
            if len(a)>len(b):
                return len(a)
            else:
                return len(b)
        else:
            return -1
        