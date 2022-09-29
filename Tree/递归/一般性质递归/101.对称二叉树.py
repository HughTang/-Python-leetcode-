#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 返回self.isSymmetricStartWithRoot的结果，旨在将root的左右子树进行拆分
        return self.isSymmetricStartWithRoot(root.left, root.right)
    
    def isSymmetricStartWithRoot(self, root1:TreeNode, root2:TreeNode) -> bool:
        # 遍历结束条件，递归返回的情况为and，因此为了不影响遍历
        # 结束时的结果，需要返回True
        if not root1 and not root2:
            return True
        # 递归终止条件1：两树结构不同
        if not root1 or not root2:
            return False
        # 递归终止条件2：两树对应节点的值不同
        if root1.val != root2.val:
            return False
        # 递归返回
        return self.isSymmetricStartWithRoot(root1.left, root2.right) and self.isSymmetricStartWithRoot(root1.right,root2.left)
# @lc code=end

