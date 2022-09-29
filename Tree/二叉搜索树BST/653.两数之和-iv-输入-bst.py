#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # 接收中序遍历所得的有序列表
        result = self.inorderTraversal(root)
        
        # 哈希表法
        # hashmap = dict()
        # for i,v in enumerate(result):
        #     if k-v in hashmap:
        #         return True
        #     hashmap[v] = i
        # return False
        
        # 双指针法（优化）
        i, j = 0, len(result)-1
        while i < j:
            num = result[i] + result[j]
            if num == k:
                return True
            if num < k:
                i += 1
            else:
                j -= 1
        return False

    # 中序遍历
    def inorderTraversal(self, root: TreeNode):
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

