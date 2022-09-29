#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # 1.计算链表长度length
        # 2.每个链表初始元素个数width = length // k
        # 3.余数remainder = length % k
        # 4.分隔链表
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        width = length // k
        remainder = length % k

        ans = list()
        cur = head
        for i in range(k):
            ans.append(cur)
            # 本题的关键在于range中的循环条件
            for _ in range(width + (i < remainder) - 1):
                cur = cur.next
            if cur:
                tmp = cur.next
                cur.next = None
                cur = tmp
        return ans
# @lc code=end

