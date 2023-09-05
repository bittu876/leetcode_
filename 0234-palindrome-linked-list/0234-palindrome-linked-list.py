# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst=[]
        temp=head
        while temp!=None:
            lst.append(str(temp.val))
            temp=temp.next
        x="".join(lst)
        lst1=[]
        for i in range(len(x)-1,-1,-1):
            lst1.append(x[i])
        y="".join(lst1)
        if x == y:
            return True
        else:
            return False

        