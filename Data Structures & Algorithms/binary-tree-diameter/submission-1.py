# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = self.findHeight(root.left) + self.findHeight(root.right)
        return max(res, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def findHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.findHeight(root.left), self.findHeight(root.right))