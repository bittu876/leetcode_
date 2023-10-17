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
        ref = pre(root)
        min_dis = 999999
        for i in range(len(res)):
            for j in range(i+1, len(res)):
                if abs(res[i] - res[j]) < min_dis:
                    min_dis = abs(res[i] - res[j])
        return min_dis
        