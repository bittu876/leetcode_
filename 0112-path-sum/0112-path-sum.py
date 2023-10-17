# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def check(node,sum1,targetSum):
            res = False
            if node.left == None and node.right == None:               
                if sum1+node.val == targetSum:
                    res =  True
                    return res         
            elif node.left == None and node.right != None:
                return check(node.right,sum1+node.val,targetSum)
            elif node.left != None and node.right == None:
                return check(node.left,sum1+node.val,targetSum)
            else:
                return check(node.right,sum1+node.val,targetSum) or check(node.left,sum1+node.val,targetSum)
                
        if root == None:
            return 0
        return check(root,0,targetSum)
        