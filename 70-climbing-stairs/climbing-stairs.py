class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        a,b=1,2
        for i in range(3,n+1):
            cur=a+b
            a,b=b,cur
        return b
        