class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=len(s)
        l=0
        r=a-1
        s=list(s)
        vow=list("aeiouAIEOU")
        while l<r:
            while l<r and s[l] not in vow:
                l+=1
            while r>l and s[r] not in vow:
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)
        