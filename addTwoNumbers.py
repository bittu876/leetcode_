#2. Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/submissions/

class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addTwoNumbers(l1, l2):
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
n1=int(input("enter  first number"))
n2=int(input("enter second number"))

ls1=ListNode()
ls1.val=n1%10
n1=n1//10
l1=ls1
while n1!=0:
            ls1.next=ListNode()
            ls1=ls1.next
            ls1.val=n1%10
            n1=n1//10
ls2=ListNode()
ls2.val=n2%10
n2=n2//10
l2=ls2
while n2!=0:
            ls2.next=ListNode()
            ls2=ls2.next
            ls2.val=n2%10
            n2=n2//10

result=addTwoNumbers(l1, l2)
print("the result in revers order is")

while result!=None:
    print(result.val ,end=" ")
    result=result.next
    


                     

