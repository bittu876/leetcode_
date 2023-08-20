# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        ref=[]
        while temp != None:
            ref.append(temp.val)
            temp = temp.next
        ref.sort()
        if len(ref) == 0:
            res=ListNode("",)
            return res
        res_lst=ListNode()
        res=ListNode()
        res=res_lst
        count=0
        while count < len(ref):
            res_lst.val=ref[count]
            count+=1
            if count < len(ref):
               res_lst.next=ListNode(ref[count],)
               res_lst=res_lst.next
            
            
                
        return res