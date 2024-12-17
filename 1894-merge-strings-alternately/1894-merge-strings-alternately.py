class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        q=len(word1)
        w=len(word2)
        if q<=w:
            a=""
            for i in range(q):
                c=word1[i]+word2[i]
                a=a+c
            b=a+word2[q:]        
        else:
            a=""
            for i in range(w):
                c=word1[i]+word2[i]
                a=a+c
            b=a+word1[w:]
        return b