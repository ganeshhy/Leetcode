# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        leftptr=head
        rightptr=head
        while rightptr is not None and rightptr.next is not None:
            leftptr=leftptr.next
            rightptr=rightptr.next.next
        return leftptr
        