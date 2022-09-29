#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路：分治+中序遍历优化
    # 由于构造出的二叉搜索树的中序遍历结果就是链表本身，因此
    # 我们可以将分治和中序遍历结合起来，减少时间复杂度。
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.head = head
        length = 0
        while head:
            length += 1
            head = head.next
        return self.toBST(0,length-1)
    
    def toBST(self, low: int, high: int) -> TreeNode:
        if low > high:
            return None
        mid = (low + high) // 2
        root = TreeNode()
        root.left = self.toBST(low,mid-1)
        root.val = self.head.val
        self.head = self.head.next
        root.right = self.toBST(mid+1,high)
        return root

# @lc code=end

