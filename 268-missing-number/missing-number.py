class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sumlen=(n*(n+1))//2
        a=sum(nums)
        
        return sumlen-a