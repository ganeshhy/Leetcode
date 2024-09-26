class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a=len(nums)
        if nums[0]!=0:
            return 0
        if nums[-1]!=a:
            return a
        for i in range(1,len(nums)):
            if nums[i]!=i:
                return i
        return 0


        