#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 使用递归完成二叉搜索树的修剪
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 遍历终止条件
        if not root:
            return None
        # 递归终止条件1：节点的值小于最小值，返回其右子树的修剪结果
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 递归终止条件2：节点的值大于最大值，返回其左子树的修剪结果
        if root.val > high:
            return self.trimBST(root.left, low, high)
        # 若节点值在规定范围内，则将该节点左右子树的修剪结果重新赋值给左右子树
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        # 返回根节点
        return root
# @lc code=end

