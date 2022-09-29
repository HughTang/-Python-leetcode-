#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 树的判空
        if not root:
            return 0
        # 定义队列用于存取层次遍历中树的节点
        queue = list()
        # 将根节点入队
        queue.insert(0, root)
        # 队列判空循环
        while queue:
            # length用于存放当前队列的长度
            length = len(queue)
            # ans被赋值为当前层的最左侧节点的值
            ans = queue[-1].val
            # 对当前层的所有节点进行处理，若有左右及节点，则将其入队
            for _ in range(length):
                node = queue.pop()
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
        # 返回最后一层的最左边的节点结果值
        return ans
# @lc code=end

