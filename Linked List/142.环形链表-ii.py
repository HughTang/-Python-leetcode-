#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
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
    def detectCycle(self, head: ListNode) -> ListNode:
        hash = set()
        while head:
            if head in hash:
                return head
            hash.add(head)
            head = head.next
        return None
    
    # 方法二：快慢指针
    # 时间复杂度为O(N)，空间复杂度为O(1)
    # 思路推导：
    # 当slow与fast第一次相遇时，
    # （1）fast走的步数是slow步数的2倍，即 f = 2s
    # （2）fast比slow多走了n个环的长度，即 f = s + nb
    # 以上两式相减得：f = 2nb，s = nb
    # 如果让指针从链表头部一直向前走并统计步数k，那么所有 走到链表入口节点时的步数 是：k=a+nb（先走a步到入口节点，之后每绕1圈环（b步）都会再次到入口节点）。
    # 而目前，slow 指针走过的步数为 nb 步。因此，我们只要想办法让 slow 再走 a 步停下来，就可以到环的入口。
    # 因此，可以另slow指针位置不变，将fast指针重新指向链表头部节点；slow和fast同时每轮向前走 1 步，此时 f = 0，s = nb；
    # 当 fast 指针走到f = a 步时，slow 指针走到步s = a+nb，此时两指针重合，并同时指向链表环入口。
    # 最后返回slow指针指向的节点即可。
    # 题解网址：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
# @lc code=end

