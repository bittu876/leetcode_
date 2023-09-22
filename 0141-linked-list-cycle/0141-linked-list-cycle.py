# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        check=[]
        temp=head
        while temp!=None:
            if temp.next == None:
                return False
            if temp.next in check:
                return True
            check.append(temp.next)
            temp=temp.next
        return False
            