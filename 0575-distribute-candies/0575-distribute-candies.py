class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        a=len(list(set(candyType)))
        b=len(candyType)/2
        return min(a,b)
        
        