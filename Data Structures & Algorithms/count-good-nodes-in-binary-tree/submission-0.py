# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [root]
        max = [root.val]
        count = 0

        while stack:
            node = stack.pop()
            maxVal = max.pop()

            if node and node.val >= maxVal:
                maxVal = node.val
                count += 1
            if node:
                max.append(maxVal)
                max.append(maxVal)
                stack.append(node.left)
                stack.append(node.right)

        return count