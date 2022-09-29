#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 先使用中序遍历获取有序数组，然后计算其相邻元素之差绝对值的最小值
    def getMinimumDifference(self, root: TreeNode) -> int:
        ls = self.InOrder(root)
        ans = ls[1] - ls[0]
        for i in range(1, len(ls)-1):
            diff = abs(ls[i+1] - ls[i])
            if diff < ans:
                ans = diff
        return ans
            

    def InOrder(self, root: TreeNode) -> List[int]:
        result = list()
        stack = list()
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node.val)
            cur = node.right
        return result
# @lc code=end

