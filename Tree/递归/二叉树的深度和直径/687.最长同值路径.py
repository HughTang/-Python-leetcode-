#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # result用于存放最终的返回结果
    def __init__(self, result = 0):
        self.result = result
    
    # 调用dfs函数，并返回self.result
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result
    
    # 深度优先遍历函数
    def dfs(self, root:TreeNode) -> int:
        # 遍历结束条件
        if not root:
            return 0
        
        # left和right分别为左子树和右子树的最长同值路径
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        # left_path用于存放根节点的值与左节点的值相等的情况，
        # 相等则赋值为左子树的最长同值路径left+1，否则赋值为0
        left_path = left + 1 if root.left and root.left.val == root.val else 0

        # right_path用于存放根节点的值与右节点的值相等的情况，
        # 相等则赋值为右子树的最长同值路径right+1，否则赋值为0
        right_path = right + 1 if root.right and root.right.val == root.val else 0
        
        # 最终结果result为原result和left_path+right_path的最大值
        self.result = max(self.result, left_path + right_path)
        
        # 返回left_path和right_path中的最大值
        return max(left_path,right_path)
# @lc code=end

