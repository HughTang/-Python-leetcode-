#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # None节点直接返回0
        if not root:
            return 0
        # 返回当前根节点的符合条件的路径数目，遍历每个节点返回符合条件的路径数目
        ans = self.pathSumStartWithRoot(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return ans

    def pathSumStartWithRoot(self, root:TreeNode, sum:int) -> int:
        # None节点直接返回0
        if not root:
            return 0
        # ret归0
        ret = 0
        # 到达末节点整好与sum相等，则ret++
        if root.val == sum:
            ret += 1
        # 遍历根节点的左子树右子树，返回符合条件的路径数目，并且与前面的ret相加
        ret += self.pathSumStartWithRoot(root.left, sum - root.val) + self.pathSumStartWithRoot(root.right, sum - root.val)
        # 返回以当前节点为根节点的符合条件的总路径数目
        return ret
# @lc code=end

