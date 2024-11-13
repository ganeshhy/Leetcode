class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans=0
        total=0
        for i in timeSeries:
            ans+=i+duration-max(i,total)
            total=i+duration
        return ans
        