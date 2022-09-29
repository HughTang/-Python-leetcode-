#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 前序遍历为root->left->right，后序遍历为left->right->root。
    # 可以修改前序遍历成为 root -> right -> left，那么这个顺序就
    # 和后序遍历正好相反。
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        ans = list()
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans[::-1]
# @lc code=end

