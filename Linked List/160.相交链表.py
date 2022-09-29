#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 相交时：设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
    # 不相交：如果不存在交点，那么 a + b = b + a，以下实现代码中 l1 和 l2 会同时为 null，从而退出循环。
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
    # 以下为借用哈希表的方法，不推荐
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     hash1 = set()
    #     while headA:
    #         hash1.add(headA)
    #         headA = headA.next
    #     hash2 = set()
    #     while headB:
    #         if headB in hash1:
    #             return headB
    #         hash2.add(headB)
    #         headB = headB.next
    #     return None
# @lc code=end

