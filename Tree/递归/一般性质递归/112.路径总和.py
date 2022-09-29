#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 在递归结构中，递归函数可以看成可以完成子问题的封闭函数，
    # 并且能够返回子问题的结果，然后根据为分解结果进行组合。
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 当遇到None节点时返回False
        if not root:
            return False
        # 但遇到叶子结点时，判断经过子问题路径递减之后的targetSum
        # 的值是否与当前叶子结点的val相等，相等则返回True
        if not root.left and not root.right:
            return root.val == targetSum
        # 递归结构设计，递归计算左子树和右子树的路径之和
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
# @lc code=end