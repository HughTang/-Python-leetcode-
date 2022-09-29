#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 遍历终止条件
        if not root:
            return 0
        # 分别获取左子树和右子树的最小深度
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        # 如果某节点不包含左子树或者右子树，则返回l+r+1
        if l == 0 or r == 0:
            return l + r + 1
        # 返回l和r中的最小值并+1
        return min(l,r) + 1
# @lc code=end