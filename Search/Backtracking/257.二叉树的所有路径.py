#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 处理特殊情况
        if not root:
            return []
        # 初始化结果列表
        ans = []
        self.dfs(root,ans,'')
        return ans
    
    # DFS中最重要的是path参数，用于保存每个路径的实时路径结果，ans为最终结果列表
    def dfs(self, root:TreeNode, ans: List[str], path: str):
        # 递归出口：遍历到叶子节点时，将该路径加入ans中，并返回
        if not root.left and not root.right:
            ans.append(path+str(root.val))
            return 
        # DFS递归左子树
        if root.left:
            self.dfs(root.left, ans, path+str(root.val)+'->')
        # DFS递归左子树
        if root.right:
            self.dfs(root.right, ans, path+str(root.val)+'->')
# @lc code=end

