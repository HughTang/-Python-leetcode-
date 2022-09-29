#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 方法一：哈希表
    # 时间复杂度和空间复杂度都为O(N)
    def hasCycle(self, head: ListNode) -> bool:
        hash = set()
        while head:
            if head in hash:
                return True
            hash.add(head)
            head = head.next
        return False
    
    # 方法二：快慢指针
    # 时间复杂度为O(N)，空间复杂度为O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while True:
            if not fast or not fast.next: 
                return False
            fast, slow = fast.next.next, slow.next
            if fast == slow: 
                return True
# @lc code=end

