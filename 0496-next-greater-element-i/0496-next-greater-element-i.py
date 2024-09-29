class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums1)):
            max_num=-1
            for j in range(len(nums2)):
                index=j
                if nums1[i]==nums2[j]:
                    while index!=len(nums2):
                        if nums2[index]>nums1[i]:
                            max_num=nums2[index]
                            break
                        index+=1
            res.append(max_num)
        return res
        """rs=[]
        for i in num1:
            for j in num2:
                if num1[i]==num2[j]:
                    if num2[j+1]>num1[i]:"""
                        
        