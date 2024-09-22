class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid+1]>nums[mid]:
                l=l+1
            else:
                r=mid
        return l
        