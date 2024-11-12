class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums=sorted(set(nums))
        
        j=0
        res=[]
        for i in range(1,n+1):
            if j<len(nums) and i==nums[j]:
                j+=1
            else:
                res.append(i)
        return res
        