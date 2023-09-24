# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return ListNode('')
        temp = head
        res=[]
        while temp!=None:
            res.append(temp.val)
            temp = temp.next
        if k%len(res) == 0:
            return head
        for i in range(k%len(res)):
            res=res[len(res)-1:]+res[:len(res)-1]
        result =ListNode()
        i = 0
        while i < len(res):
            if i == 0:
                res1 = ListNode(res[i])
                result = res1
            else:
                res1.next = ListNode()
                res1 = res1.next
                res1.val = res[i]
                if i == len(res) -1:
                    res1.next = None
                else:
                    res1.next = ListNode()
            i = i + 1
        return result

        


                