# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res=[]
        temp = head
        while temp != None:
            if temp.val != val:
                res.append(temp.val)
            temp = temp.next
        if len(res) == 0:
            return ListNode("",None)
        ref = ListNode()
        i = 0
        while i < len(res):
            if  i == 0:
                temp = ListNode(res[i])
                ref = temp
                if i == len(res)-1:
                   temp.next = None
                else:
                    temp.next = ListNode()
            else:
                temp = temp.next
                temp.val = res[i]
                if i == len(res) - 1:
                    temp.next = None
                else:
                    temp.next = ListNode()
            i += 1
        return ref