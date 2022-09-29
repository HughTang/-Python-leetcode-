# 题目描述：
# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = list()

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        ret = list()
        self.dfs(root,target,ret)
        return self.result
    
    def dfs(self,root:TreeNode, target:int, ret:list) -> int:
        if not root:
            return 0
        ret.append(root.val)
        target -= root.val
        if not root.left and not root.right and target == 0:
            self.result.append(list(ret))
        else:
            self.dfs(root.left, target, ret)
            self.dfs(root.right, target, ret)
        ret.pop()
        