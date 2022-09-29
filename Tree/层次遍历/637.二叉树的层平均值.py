#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 经典层次遍历问题，需要借助队列进行遍历节点的存取，
    # 这里需要注意的是queue的存取是怎样借助list操作完成的
    # 入队：queue.insert(0, node)
    # 出队：queue.pop()
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # ans用于存放
        ans = list()
        # 定义队列，用于存取节点
        queue = list()
        # 树的判空
        if not root:
            return ans
        # 将根节点入队
        queue.insert(0, root)
        # 队列判空循环
        while queue:
            # num初始化，用于存放每层节点的值的和
            num = 0
            # 获取当前队列的长度
            length = len(queue)
            # 当前队列中节点的循环处理
            for _ in range(length):
                # 出队赋值给node
                node = queue.pop()
                # num的加法处理
                num += node.val
                # 判断出队节点的左子树是否为空，不为空则入队
                if node.left:
                    queue.insert(0, node.left)
                # 判断出队节点的右子树是否为空，不为空则入队
                if node.right:
                    queue.insert(0, node.right)
            # 将每层的节点的平均值加入结果列表ans中
            ans.append(num / length)
        # 返回结果列表
        return ans
# @lc code=end

