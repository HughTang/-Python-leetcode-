#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 为了优化时间复杂度，在中序遍历过程中，就需要将出现元素的
    # 最高频率记录下来，并将符合条件的元素记录在列表result中，
    # 解题的重点在于记录中序遍历的上一个节点元素pre_node，以及
    # 实时更新cur_len和max_len。
    def findMode(self, root: TreeNode) -> List[int]:
        result = self.InOrder(root)
        return result

    def InOrder(self, root: TreeNode) -> List[int]:
        result = list()
        stack = list()
        cur = root
        cur_len = 1
        max_len = 1
        pre_node = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            cur = node.right

            if pre_node:
                cur_len = cur_len + 1 if pre_node.val == node.val else 1
            if cur_len > max_len:
                max_len = cur_len
                result.clear()
                result.append(node.val)
            elif cur_len == max_len:
                result.append(node.val)
            pre_node = node

        return result
# @lc code=end

