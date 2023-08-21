# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        ref_lst=ListNode()
        ref_lst=head
        lst=[]
        while ref_lst != None:
            lst . append(ref_lst.val)
            ref_lst=ref_lst.next
        print(lst)
        if not lst:
           return None
        def check(min,max):
            if min > max:
                return None
            mid=(min+max)//2
            tree=TreeNode(lst[mid])
            tree.left=check(min,mid-1)
            tree.right=check(mid+1,max)
            
            return tree
        
       
        return  check(0,len(lst)-1)