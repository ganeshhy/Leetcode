class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a={}
        for cur_ind,cur_num in enumerate(nums):
            if cur_num in a:
                if cur_ind-a[cur_num]<=k:
                    return True
            a[cur_num]=cur_ind
        return False
        