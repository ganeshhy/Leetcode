class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=set(range(1,len(nums)+1))
        y=set(nums)
        return list(x-y)
        