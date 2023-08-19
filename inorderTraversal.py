

# 94. Binary Tree Inorder Traversal

# https://leetcode.com/problems/binary-tree-inorder-traversal/
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def inorderTraversal( root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def checkInorder(root):
            if root == None:
                return
            checkInorder(root.left)
            res.append(root.val)
            checkInorder(root.right)
        checkInorder(root)
        return res
root=TreeNode(5,TreeNode(3,TreeNode(1,None,None),TreeNode(8,None,None)),TreeNode(1,TreeNode(1,None,None),TreeNode(1,None,None)))
x=inorderTraversal(root)
print(x)

