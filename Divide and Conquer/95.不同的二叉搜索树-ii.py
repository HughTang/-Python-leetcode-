#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 分治思想
    # （1）能够解决的子问题：单个节点的值和空结点None
    # （2）如何拆分：以1到n的每个数字作为头结点进行拆分
    # （3）如何合并：将左右子树集合中的子树分别与当前数字i的头结点相联结，并加入到最终结果集合
    def generateTrees(self, n: int) -> List[TreeNode]:
        # 如果n为0，则返回[]；n不为0，则返回递归函数helper的结果
        return self.helper(1,n) if n else []
    
    def helper(self, start: int, end: int):
        # 递归终止条件
        if start > end:
            return [None]
        
        # 初始化ans存放最终结果集合
        ans = list()
        # 遍历每个数字，递归处理i为头结点的情况
        for i in range(start, end+1):
            # 获取i的左子树
            left = self.helper(start, i-1)
            # 获取i的右子树
            right = self.helper(i+1, end)
            # 遍历left和right的左右子树集合，使其分别与头结点i连接，从而获得不同的二叉搜索树
            for l in left:
                for r in right:
                    node = TreeNode(i,l,r)
                    ans.append(node)
        # 返回最终结果集合
        return ans
# @lc code=end

