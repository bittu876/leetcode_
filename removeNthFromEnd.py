
#19. Remove Nth Node From End of List
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lenth=0
        temp=head
        while temp!=None:
            lenth+=1
            temp=temp.next
        if lenth==1:
            ls=ListNode()
            ls.val=""
            return ls
        if lenth-n==0:
            x=ListNode()
            x=head.next
            return x    
        x=ListNode()
        x=head
        ls=x
        count=0
        while x!=None:
            count+=1
            if count==lenth-n:  
                y=ListNode()
                y=x.next
                x.next=y.next 
                break
            x=x.next       
        return ls

head=ListNode(3,ListNode(6,ListNode(7,ListNode(5,ListNode(9,ListNode(8,None))))))
n=2
result=removeNthFromEnd(head, n)
tempe=ListNode()
tempe=result
while tempe!=None:
    print(tempe.val,end=" ")
    tempe=tempe.next
