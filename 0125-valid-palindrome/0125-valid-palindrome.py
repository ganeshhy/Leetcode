import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=s.lower()
        
        b = re.sub(r'[^a-z0-9]', '', a)
        c=list(b)
        if len(c)<=1:
            return True
        i=0
        j=len(c)-1
        is_pali=True
        
        while i<j:
            if c[i]!=c[j]:
                is_pali=False
                break
            i+=1
            j-=1
        if is_pali:
            return True
        else:
            return False

        