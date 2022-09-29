#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 方法一：反向中序遍历（right->root->left），每个节点
    # 修改后的val=node.val+右子树的节点之和num
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = list()
        if not root:
            return root
        cur = root
        # 用于存储每个节点右子树的节点值之和
        num = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            node = stack.pop()
            node.val += num
            num = node.val
            cur = node.left
        return root
    
    # 方法二：递归
    def __init__(self, num=0):
        self.num = num

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.BST(root)
        return root
    
    def BST(self, root: TreeNode) -> None:
        if not root:
            return
        self.BST(root.right)
        root.val += self.num
        self.num = root.val
        self.BST(root.left)
# @lc code=end

