class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ls=sorted(score,reverse=True)
        n=len(ls)
        ans={}
        for i in range(n):
            if i==0:
                ans[ls[i]]="Gold Medal"
            elif i==1:
                ans[ls[i]]="Silver Medal"
            elif i==2:
                ans[ls[i]]="Bronze Medal"
            else:
                ans[ls[i]]=str(i+1)
        res=[]
        for i in score:
            res.append(ans[i])
        return res

