# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1=headA
        temp2=headB
        while (temp1!=temp2):
            temp1=headB if not  temp1 else temp1.next
            
            temp2=headA if not temp2  else temp2.next
        return temp1


        