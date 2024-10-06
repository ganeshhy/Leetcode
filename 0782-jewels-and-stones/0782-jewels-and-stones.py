class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        a=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                a+=1
        return a
        