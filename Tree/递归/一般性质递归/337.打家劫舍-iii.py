#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        分治递归处理“偷当前节点”与“不偷当前节点”两种情况
    '''
    def rob(self, root: TreeNode) -> int:
        return max(self.robRecursion(root))
    
    def robRecursion(self, root: TreeNode):
        if not root:
            return 0, 0  #偷, 不偷
        
        # left和right分别用来存储返回的左右子树中的偷与不偷的列表
        left = self.robRecursion(root.left)
        right = self.robRecursion(root.right)
        
        # 偷当前节点，则其左右节点均不偷
        val1 = root.val + left[1] + right[1]

        # 不偷当前节点，则偷其左右子树中最大的值之和
        val2 = max(left) + max(right)

        # 返回偷与不偷的结果
        return val1, val2
# @lc code=end

