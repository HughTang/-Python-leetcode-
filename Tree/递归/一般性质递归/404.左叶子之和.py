#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 遍历终止条件
        if not root:
            return 0
        # 递归终止条件：判断该节点为左叶子节点的父节点，并返回
        # 左叶子节点的值+父节点右子树所有左叶子节点的值
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        # 递归返回左右子树中存在的左叶子节点的值之和
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
# @lc code=end

