class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))
        b=sorted(a,reverse=True)
        
        if len(a)<3:

            return max(a)
        elif len(a)>=3:
            return b[2]



        