class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        su=[1]*n
        pr=[1]*n
        for i in range(1,n):
            pr[i]=pr[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            su[j]=su[j+1]*nums[j+1]
        res=[]
        for i in range(n):
            ans=pr[i]*su[i]
            res.append(ans)
        return res

        