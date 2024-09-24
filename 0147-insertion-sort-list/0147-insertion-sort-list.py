# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums=[]
        cur=ans =head
        while head:
            nums.append(head.val)
            head=head.next
        nums=sorted(nums)
        count=0
        while cur:
            cur.val=nums[count]
            count+=1
            cur=cur.next
        return ans

        