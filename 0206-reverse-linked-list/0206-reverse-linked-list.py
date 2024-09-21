# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_node=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=new_node
            new_node=cur
            cur=temp
        return new_node
    
        