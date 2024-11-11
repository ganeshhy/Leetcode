class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1=set(sorted(nums1))
        n2=set(sorted(nums2))
        n1=list(n1)
        n2=list(n2)
        a=[]
        for i in range(len(n1)):
            for j in range(len(n2)):
                if n1[i]==n2[j]:
                    a.append(n1[i])
        return a
