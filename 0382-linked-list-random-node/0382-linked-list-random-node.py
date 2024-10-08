# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head=head
        

    def getRandom(self):
        """
        :rtype: int
        """
        ans=0
        p,i=self.head,0
        while p:
            if random.randint(0,i)==0:
                ans=p.val
            p=p.next
            i+=1
        return ans
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()