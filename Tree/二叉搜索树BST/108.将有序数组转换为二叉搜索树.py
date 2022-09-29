#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 本题的思路在于折半插入，每次递归都将nums数组的最中间值作为节点插入
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.toBST(nums,0,len(nums)-1)
    
    def toBST(self, nums: List[int], low: int, high: int) -> TreeNode:
        if low > high:
            return None
        mid = (low + high) // 2
        root = TreeNode(nums[mid])
        root.left = self.toBST(nums,low,mid-1)
        root.right = self.toBST(nums,mid+1,high)
        return root
# @lc code=end