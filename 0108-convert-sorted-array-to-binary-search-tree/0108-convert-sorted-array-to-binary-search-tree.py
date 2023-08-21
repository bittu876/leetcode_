# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def binaryTree(min,max):
            if max < min:
                return None
            mid=(min + max) // 2
            tree=TreeNode(nums[mid])
            tree.left=binaryTree(min,mid - 1)
            tree.right=binaryTree(mid + 1,max)
            return tree
        root=binaryTree(0,len(nums)-1)
        return root