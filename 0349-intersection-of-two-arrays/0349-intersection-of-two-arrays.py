class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=set(nums1)
        b=set(nums2)
        re=[]
        for num in a:
            if num  in b:
                re.append(num)
        return re

        