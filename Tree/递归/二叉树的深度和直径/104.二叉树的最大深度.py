#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    如果我们知道了左子树和右子树的最大深度l和r，那么该二叉树的
    最大深度即为max(l,r)+1,而左子树和右子树的最大深度又可以以
    同样的方式进行计算。因此我们可以用「深度优先搜索」的方法来
    计算二叉树的最大深度。具体而言，在计算当前二叉树的最大深度
    时，可以先递归计算出其左子树和右子树的最大深度，然后在O(1)
    时间内计算出当前二叉树的最大深度。递归在访问到空节点时退出。
    该方法的时间复杂度为O(N)，空间复杂度为O(height)。
    '''
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        r = self.maxDepth(root.right)
        l = self.maxDepth(root.left)
        return max(r,l) + 1
# @lc code=end

