#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, result = 0):
        self.result = result
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDepth(root)
        return self.result
    
    def maxDepth(self, root:TreeNode) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        # 重点是获取每次递归次数所处根节点的最大左右子树的深度值之和
        self.result = max(self.result, l + r)
        return max(l,r) + 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
# @lc code=end

