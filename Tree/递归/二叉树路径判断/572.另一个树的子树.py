#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 由于此函数递归时的return结果取or，所以递归到结尾时
        # 应该返回False，不影响判断结果
        # 遍历结束条件
        if not s:
            return False
        # 将s的每个节点都作为根节点去传到isSubtreeWithRoot中，并取or
        return self.isSubtreeWithRoot(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def isSubtreeWithRoot(self, s: TreeNode, t: TreeNode) -> bool:
        # 由于此函数递归时的return结果取and，所以递归到结尾时
        # 应该返回True，不影响判断结果
        # 遍历结束条件
        if not s and not t:
            return True
        # 递归终止条件1：两树结构不符
        if not s or not t:
            return False
        # 递归终止条件2：两数同位置节点的值不相等
        if s.val != t.val:
            return False
        # 将s作为根节点，同时遍历s与t，判断两树的结构和值是否相等，并取and
        return self.isSubtreeWithRoot(s.left,t.left) and self.isSubtreeWithRoot(s.right,t.right)
        
# @lc code=end