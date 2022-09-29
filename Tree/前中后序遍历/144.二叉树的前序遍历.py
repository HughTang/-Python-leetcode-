#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        ans = list()
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            # 先右后左，保证出栈时先遍历左子树
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans
# @lc code=end

