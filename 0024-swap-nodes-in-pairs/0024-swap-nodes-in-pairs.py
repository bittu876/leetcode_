# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        ref = []
        while temp !=None:
            ref.append(temp.val)
            temp =temp.next
        j = 0
        k=1
        temp1=0
        while j <len(ref) and k<len(ref):
            ref[j],ref[k] =ref[k],ref[j]
            j=j+2
            k=k+2
        l = 0  
        result = ListNode("")
        while l < len(ref):
            if l == 0:
                resl = ListNode(ref[l])
                result = resl
                l =l+1
            else:  
                resl.next = ListNode(ref[l])
                resl = resl.next
                l = l + 1

        return result
            
            

        
           