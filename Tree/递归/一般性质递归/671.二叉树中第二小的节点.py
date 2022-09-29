#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 此题主要有三个递归细节：
    # （1）遍历终止条件2个
    # （2）根节点值与左右孩子节点的值是否相等（递归之处）
    # （3）left和right是否为-1（是否满足题目要求）的判断
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 遍历终止条件1：节点为空
        if not root:
            return -1
        
        # 遍历终止条件2：叶子结点
        if not root.left and not root.right:
            return -1
        
        # left和right分别被赋值为根节点的左节点值和右节点值
        left = root.left.val
        right = root.right.val
        
        # 判断根节点的值与左孩子节点的值是否相等，相等的话left
        # 被重新赋值为root.left的递归形式
        if left == root.val:
            left = self.findSecondMinimumValue(root.left)
        # 判断根节点的值与右孩子节点的值是否相等，相等的话right
        # 被重新赋值为root.right的递归形式
        if right == root.val:
            right = self.findSecondMinimumValue(root.right)
        
        # 若left和right都不等于-1，说明左右两边都有比根节点大的第二小的节点
        if left != -1 and right != -1:
            return min(left,right)
        
        # 若left不等于-1，说明左子树中有比根节点大的第二小的节点
        if left != -1:
            return left
        
        # 最后这个返回包含了两种情况：
        # （1）right!=-1直接返回左子树中比根节点大的第二小的节点的值
        # （2）right==-1直接返回-1
        return right
# @lc code=end

