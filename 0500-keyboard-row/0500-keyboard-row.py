class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a={'q','w','e','r','t','y','u','i','o','p'}
        b= {'a','s','d','f','g','h','j','k','l'}
        c = {'z','x','c','v','b','n','m'}
        res=[]
        for i in words:
            set1=set(i.lower())
            if (set1&a==set1 or set1&b==set1 or set1&c==set1):
                res.append(i)
        return res