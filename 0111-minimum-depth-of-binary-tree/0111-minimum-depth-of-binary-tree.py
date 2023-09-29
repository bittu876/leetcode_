# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node):
                if node.left == None and node.right == None:
                    return 1
                elif node.left == None and node.right != None:
                    return check(node.right)+1
                elif node.left != None and node.right == None:
                    return check(node.left)+1
                else:
                    return min(check(node.right) , check(node.left))+1
        if root == None:
            return 0
        return check(root)