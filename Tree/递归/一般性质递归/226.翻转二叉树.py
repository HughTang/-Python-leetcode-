#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    （1）递归思想：
        我们从根节点开始，递归地对树进行遍历，并从叶子结点先开始
    翻转。如果当前遍历到的节点root的左右两棵子树都已经翻转，那么
    我们只需要交换两棵子树的位置，即可完成以root为根节点的整棵子
    树的翻转。
    （2）时间复杂度：
        O(N)，其中N为二叉树节点的数目。我们会遍历二叉树中的每一个
    节点，对每个节点而言，我们在常数时间内交换其两棵子树。
    （3）空间复杂度：
        O(N)，使用的空间由递归栈的深度决定，它等于当前节点在二叉
    树中的高度。在平均情况下，二叉树的高度与节点个数为对数关系，
    即O(log N)。而在最坏情况下，树形成链状，空间复杂度为O(N)。
    '''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root
# @lc code=end

