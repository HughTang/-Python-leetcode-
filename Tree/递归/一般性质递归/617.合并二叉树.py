#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        两个二叉树的对应节点可能存在以下三种情况，对于每种情况使用不同的合并方式。
        （1）如果两个二叉树的对应节点都为空，则合并后的二叉树的对应节点也为空；
        （2）如果两个二叉树的对应节点只有一个为空，则合并后的二叉树的对应节点为其中的非空节点；
        （3）如果两个二叉树的对应节点都不为空，则合并后的二叉树的对应节点的值为两个二叉树的对应节点的值之和，此时需要显性合并两个节点。
    '''
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # if not root1 and not root2:
        #     return None
        # elif not root1:
        #     return root2
        # elif not root2:
        #     return root1
        # 下面的两行相当于前面注释的几行
        if not root1 or not root2:
            return root1 or root2
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root
        
# @lc code=end

