# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        cur=head
        for i in range(1,left):
            cur=cur.next
        stack=[]
        leftptr=rightptr=cur
        for i in range(left,right+1):
            stack.append(rightptr.val)
            rightptr=rightptr.next
        for i in range(left,right+1):
            leftptr.val=stack.pop()
            leftptr=leftptr.next
        return head