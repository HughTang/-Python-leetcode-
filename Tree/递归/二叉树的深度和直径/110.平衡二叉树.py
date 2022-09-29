#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self,result=True):
        self.result = result
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.maxDepth(root)
        return self.result

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        r = self.maxDepth(root.right)
        l = self.maxDepth(root.left)
        if abs(r - l) > 1:
            self.result = False
        return max(r,l) + 1

# @lc code=end

