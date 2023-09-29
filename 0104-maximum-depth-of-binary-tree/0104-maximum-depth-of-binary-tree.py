# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node):
            if node != None:
                if node.left == None and node.right == None:
                    return 1
                return max(depth(node.left) , depth(node.right))+1
            return 0
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1 
        return max(depth(root.left) , depth(root.right))+1

            
        