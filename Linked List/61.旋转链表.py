#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    （1）先将链表闭合成环，并计算出链表的长度；
    （2）利用k % length的方式解决原始k>length的情况；
    （3）找到链表倒数第k个节点的前驱结点；
    （4）新建result引用倒数第k个节点，并将其前驱结点的next赋值为None；
    （5）返回result。
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 判断链表为空和只包含一个元素的情况
        if not head or not head.next:
            return head
        
        # （1）先将链表闭合成环，并计算出链表的长度；
        dummy = ListNode(0,head)
        cur = dummy
        length = 0
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        
        # （2）利用k % length的方式解决原始k>length的情况；
        k %= length
        
        # （3）找到链表倒数第k个节点的前驱结点；
        cur = dummy
        for i in range(1,length-k+1):
            cur = cur.next
        
        # （4）新建result引用倒数第k个节点，并将其前驱结点的next赋值为None；
        result = cur.next
        cur.next = None
        
        # （5）返回result。
        return result
# @lc code=end

