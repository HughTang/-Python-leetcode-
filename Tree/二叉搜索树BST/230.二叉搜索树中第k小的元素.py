#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 方法一：非递归中序遍历（也可以使用递归中序遍历，但性能差）
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = list()
        stack = list()
        if not root:
            return 0
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node.val)
            cur = node.right
        return result[k-1]
    
    # 方法二：递归，效率比方法一低
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 获取左子树的节点数
        left = self.count(root.left)
        # 当左子树的节点个数正好为k-1时，返回当前节点的val
        if left == k-1:
            return root.val
        # 当左子树个节点个数大于k-1时，递归调用，当前节点变为左孩子节点
        if left > k-1:
            return self.kthSmallest(root.left,k)
        # 当左子树个节点个数小于k-1时，递归调用，当前节点变为右孩子节点，k变为k-left-1
        return self.kthSmallest(root.right, k-left-1)

    # 此函数用于递归返回左子树的节点个数
    def count(self, root:TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
# @lc code=end

