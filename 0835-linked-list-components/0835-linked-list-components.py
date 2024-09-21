# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)
        cur=head
        count=0
        while cur is not None:
            if cur.val in num_set:
                if cur.next is None or cur.next.val not in num_set:
                    count+=1
            cur =cur.next
        return count

        