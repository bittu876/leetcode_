
# 100. Same Tree
# https://leetcode.com/problems/same-tree/

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSameTree (p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def check(rot):
            res=[] 
            def checkInorder(root):
                if root == None:
                    res.append("0")
                    return
                res.append(root.val)
                checkInorder(root.left)
                
                checkInorder(root.right)
            checkInorder(rot)
            return res
        if check(p)==check(q):
            return True
        else:
            return False
x=TreeNode(5,TreeNode(3,TreeNode(1,None,None),TreeNode(8,None,None)),TreeNode(1,TreeNode(1,None,None),TreeNode(1,None,None)))
y=TreeNode(5,TreeNode(3,TreeNode(1,None,None),TreeNode(8,None,None)),TreeNode(1,TreeNode(1,None,None),TreeNode(1,None,None)))
result=isSameTree(x,y)
print(result)
        
