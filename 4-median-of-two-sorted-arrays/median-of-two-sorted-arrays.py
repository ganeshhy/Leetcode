class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n=nums1
        if len(n)%2==0:
            med=n[len(n)//2-1]+n[len(n)//2]
            m=float(med)/2
            return m
        else:
            return n[len(n)//2]