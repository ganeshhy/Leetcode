class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        b=[]
        for w in a:
            c=w[::-1]
            b.append(c)
        output=' '.join(b)
        return output
        