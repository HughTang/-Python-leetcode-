#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    两个节点 p,q 分为两种情况：
    (1)p 和 q 在相同子树中
    (2)p 和 q 在不同子树中
    从根节点遍历，递归向左右子树查询节点信息
    递归终止条件：如果当前节点为空或等于p或q，则返回当前节点
    (1)递归遍历左右子树，如果左右子树查到节点都不为空，则表明 p 和 q 分别在左右子树中，因此，当前节点即为最近公共祖先；
    (2)如果左右子树其中一个不为空，则返回非空节点。
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归终止条件
        if not root or root == p or root == q:
            return root
        # left和right用于获取当前节点root的左右子树中是否含有p或q
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # 如果当前节点的左右子树都找到了p或q，则返回当前节点
        if left and right:
            return root
        # 如果左子树找到了p或q，返回left
        if left:
            return left
        # 如果右子树找到了p或q，返回right（这里省略了if语句）
        return right
# @lc code=end

