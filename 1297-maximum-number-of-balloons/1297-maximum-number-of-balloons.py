class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b=collections.Counter(text)
        return min(b['b'],b['a'],b['l']//2,b['o']//2,b['n'])
        