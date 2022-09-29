#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历为left -> root -> right
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        ans = list()
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            ans.append(node.val)
            cur = node.right
        return ans
# @lc code=end

