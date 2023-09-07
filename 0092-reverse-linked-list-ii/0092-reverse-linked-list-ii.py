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
        ref=[]
        temp = head
        while temp != None:
            ref.append(temp.val)
            temp=temp.next
        i=left -1
        j=right -1
        while i <  j:
            ref[i] , ref[j] =  ref[j] , ref[i]
            i = i + 1
            j = j - 1
        res = ListNode(ref[0])
        result =res
        k = 1
        while k < len(ref):
            res.next = ListNode()
            res = res.next
            res.val = ref[k]
            if k == len(ref) -1:
                res.next = None
            else:
                res.next = ListNode()
            k = k + 1
        return result

        