# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/



class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeTwoLists( list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst1=[]
        ls1=list1
        while ls1!=None:
            lst1.append(ls1.val)
            ls1=ls1.next
        
        lst2=[]
        ls2=list2
        while ls2!=None:
            lst2.append(ls2.val)
            ls2=ls2.next
        lst1=lst1+lst2
        lst1.sort()
        res=ListNode("",None)
        for i in range(0,len(lst1)):
            if i==0:
                ls3=ListNode()
                ls3.val=lst1[i]
                res=ls3
            else:
                ls3.next=ListNode()
                ls3=ls3.next
                ls3.val=lst1[i]
              
        return res
if __name__=="__main__":
    list1=ListNode(6,ListNode(4,ListNode(9,ListNode(20,ListNode(1,ListNode(14,None))))))
    list2=ListNode(1,ListNode(5,ListNode(8,ListNode(2,ListNode(10,ListNode(11,None))))))
    result=mergeTwoLists(list1, list2)
    temp=result
    while temp!=None:
        print(temp.val,end=" ")
        temp=temp.next
