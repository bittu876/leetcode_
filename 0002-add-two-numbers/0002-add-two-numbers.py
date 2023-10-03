# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=0
        num2=0
        count=0
        while l1!=None:
            num1=num1+l1.val * (10**count)
            count+=1
            l1=l1.next
        count=0
        while l2!=None:
            num2=num2+l2.val * (10**count)
            count+=1
            l2=l2.next
        res=num1+num2
        l3=ListNode()
        l3.val=res%10
        res=res//10
        l4=l3
        while res!=0:
            l3.next=ListNode()
            l3=l3.next
            l3.val=res%10
            res=res//10
        return l4




            

        
        
 



