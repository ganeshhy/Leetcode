# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # Find the ath node in list1
        count = 0
        current = list1
        while count < a - 1:
            current = current.next
            count += 1

        # Connect the ath node to the head of list2
        a_node = current
        while count < b + 1:
            current = current.next
            count += 1

        # Connect the last node of list2 to the node after b
        last_node_of_list2 = list2
        while last_node_of_list2.next is not None:
            last_node_of_list2 = last_node_of_list2.next
        last_node_of_list2.next = current

        # Connect the node before a to the head of list2
        a_node.next = list2

        return list1
