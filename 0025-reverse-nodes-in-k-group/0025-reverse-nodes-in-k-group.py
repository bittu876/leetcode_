# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head.next == None:
            return head
        res = []
        temp = head
        while temp != None:
            res.append(temp.val)
            temp = temp.next
        i = 0
        temp = []
        while i < len(res):
            ref = res[i:i+k]
            if len(ref) < k:
                ref = ref[::-1]
            temp = temp +ref[::-1]
            i += k
        for i in range(0,len(temp)):
            if i==0:
                ls3=ListNode()
                ls3.val=temp[i]
                res=ls3
            else:
                ls3.next=ListNode()
                ls3=ls3.next
                ls3.val=temp[i]
               
        return res
        