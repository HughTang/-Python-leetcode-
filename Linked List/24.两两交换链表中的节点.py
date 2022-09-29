#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    此题最重要的是引用（指针）的使用，可以这么理解：
    （1）p = xxx相当于指针p指向了链表的另一个节点，
        对链表本身的结构没有影响；
    （2）p.next = xxx相当于指针p所指向的链表的那个节点中
        的next变量发生了变化，对链表节点结构产生了影响。
    因此，若要对链表节点进行调整，一般是给p.next赋值更改，
    而移动指针到另一个节点，则一般通过给p赋值来实现。
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0, head)
        while pre.next and pre.next.next:
            # 分别将0连接2,1连接3，最后将2连接1，就可以了，所以需要提前用tmp保存1的位置
            tmp = pre.next
            # 0连接2
            pre.next = pre.next.next
            # 1连接3
            tmp.next = pre.next.next
            # 2连接1
            pre.next.next = tmp
            # 指针右移
            pre = pre.next.next
        return dummy.next

        # dummy = ListNode(0,head)
        # pre = dummy
        # while pre.next and pre.next.next:
        #     q = pre.next
        #     p = pre.next.next
        #     pre.next = p
        #     q.next = p.next
        #     p.next = q
        #     pre = q
        # return dummy.next
# @lc code=end

