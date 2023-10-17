# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def pre(node):
            if node == None:
                return 
            res.append(node.val)
            pre(node.left)
            pre(node.right)
            return res
        pre(root)
        min_dis = 999999
        res.sort()
        n = len(res)
        for i in range(n-1):
            if abs(res[i] - res [i+1]) < min_dis:
                min_dis = abs(res[i] - res [i+1])
        return min_dis