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
        temp = head
        res = []
        while temp != None:
            res = [temp.val] + res
            temp = temp .next
        if len(res) == 0:
            return ListNode("")
        ref = ListNode()
        i = 0
        while i<len(res):
            if i == 0:
                temp = ListNode(res[i])
                ref = temp
            else:
                temp.next = ListNode(res[i])
                temp = temp.next
            i += 1
        return ref
        