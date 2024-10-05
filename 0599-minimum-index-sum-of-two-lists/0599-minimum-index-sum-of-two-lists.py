class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        a=list(set(list1) & set(list2))
        r=[]
        b=float('inf')
        for i in a:

            c=list1.index(i)+list2.index(i)
        
            if c<b:
                r=[i]
                b=c
            elif c==b:
                r.append(i)
        return r

                    
        