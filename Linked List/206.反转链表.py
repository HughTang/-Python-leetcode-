#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 方法一：递归。假设后面的子链表已经反转，则上一次递归
        # 指向的head节点为未反转节点的倒数第二个节点，需要将其
        # 下一个节点的next（head.next.next=head）指向head，然
        # 后head.next指向None，以保证反转结束后最后节点next指
        # 向None。需要说明的是，递归的临界条件是把初始未反转链
        # 表的最后一个节点返回，作为反转后链表的头结点，在每次
        # 递归完成对每个节点next指向前一个节点后，持续接收原链
        # 表的最后一个节点，即反转链表后的头结点newHead。简单
        # 来讲，if语句中的条件只执行一次，后续都是newHead的反复
        # 递归接收头结点。其时间复杂度为O(N)，空间复杂度为O(N)。
        if not head or not head.next:
            return head

        # 由于类方法总是要在一个实例进行调用，因此在我们调用
        # 类中方法时，前面必须加self.以标识其为类的一个实例。
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


    # 方法二：迭代。采用经典头插法，新建dummy哑结点，然后
    # 遍历原链表的每个节点，将其插入到dummy.next后面。给
    # 出经典头插法的思路，见代码注释。该方法时间复杂度为
    # O(N)，空间复杂度为O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        # 新建哑结点，后续用于标识反转后的新链表
        dummy = ListNode(0)
        # cur用于遍历原链表的每个节点，此处也可以直接用head来
        # 遍历，但为了易于理解，新建一个cur指向head完成遍历
        cur = head
        
        while cur:
            # tmp用于临时存储当前节点的下一个节点的位置
            tmp = cur.next
            # 头插法中当前节点的next需要指向新链表非头结点的第
            # 一个节点位置
            cur.next = dummy.next
            # 新链表头结点的next指向当前节点cur
            dummy.next = cur
            # 将提前存储好的下一节点位置tmp赋给cur，使cur向后移动
            cur = tmp
        return dummy.next

# @lc code=end

