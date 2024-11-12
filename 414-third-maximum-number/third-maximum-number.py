class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))
        a.sort(reverse=True)
        n=len(a)
        if n<3:
            return a[0]
        else:
            return a[2]

        