# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ref = []
        temp =head 
        if head == None:
            return None
        while temp!=None:
            ref.append(temp.val)
            temp = temp.next
        res=[]
        for i in ref:
            if  i not in res:
                res.append(i)
        if len(res) == 1:
            return ListNode(res[0],None)
        temp1=ListNode()
        i = 0
        while i <len(res):
            if  i ==0:
                temp = ListNode(res[i],ListNode())
                temp1=temp
            else:
                temp = temp.next
                temp.val = res[i]
                if i == len(res) -1:
                    temp.next = None
                else:
                    temp.next = ListNode()
            i= i+1
        return temp1
        