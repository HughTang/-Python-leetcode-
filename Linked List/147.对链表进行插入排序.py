#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 判断链表是否为空
        if not head:
            return head
        # 新建哑结点，指向head
        dummy = ListNode(0,head)
        # cur用于遍历链表每个元素
        cur = head.next
        # lastnode指向已排序链表的最后一个节点，初始为head
        lastnode = head
        while cur:
            # cur所指元素大于已排序链表最后一个节点的值，lastnode往后移一位
            if lastnode.val <= cur.val:
                lastnode = lastnode.next
            else:
                # firstnode指向哑结点
                firstnode = dummy
                # 用firstnode.next进行比较来完成已排序节点的比较
                while firstnode.next.val <= cur.val:
                    firstnode = firstnode.next
                # 此处直接将cur.next赋给lastnode.next，随后进行节点插入
                lastnode.next = cur.next
                cur.next = firstnode.next
                firstnode.next = cur
            # cur指向lastnode的下一节点
            cur = lastnode.next
        # 返回head
        return dummy.next
# @lc code=end

